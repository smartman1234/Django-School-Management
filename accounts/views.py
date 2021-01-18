from rolepermissions.roles import assign_role
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView

from academics.models import Department
from students.models import Student
from teachers.models import Teacher
from .forms import (
    UserRegistrationForm,
    ProfileCompleteForm,
    ApprovalProfileUpdateForm
)
from .models import CustomGroup, User


def user_is_staff(user):
    return user.is_staff

def user_is_admin(user):
    return user.requested_role == 'admin'


@login_required(login_url='account_login')
def profile_complete(request):
    user = User.objects.get(pk=request.user.pk)
    form = ProfileCompleteForm(instance=user)
    if request.method == 'POST':
        form = ProfileCompleteForm(request.POST, instance=user)
        if form.is_valid():
            form.instance.approval_status = 'p'  # pending
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your request has been sent, please be patient.'
            )
            return redirect('account:profile_complete')
    user_permissions = user.user_permissions.all()
    ctx = {
        'form': form,
        'user_perms': user_permissions if user_permissions else None,
    }
    return render(request, 'account/profile_complete.html', ctx)


@user_passes_test(user_is_admin, login_url='account:permission_error')
def user_approval(request, pk):
    user = User.objects.get(pk=pk)
    requested_role = user.requested_role
    assign_role(user, requested_role)
    if requested_role == 'admin':
        user.is_staff = True
    user.approval_status = 'a'
    user.save()
    messages.add_message(
        request,
        messages.SUCCESS,
        f'{user}\'s account has been approved.'
    )
    return redirect('account:user_requests')


@user_passes_test(user_is_admin, login_url='account:permission_error')
def user_approval_with_modification(request, pk):
    user = User.objects.get(pk=pk)
    form = ApprovalProfileUpdateForm()
    if request.method == 'POST':
        requested_role = request.POST.get('requested_role')
        assign_role(user, requested_role)
        if requested_role == 'admin':
            user.is_staff = True
        user.approval_status = 'a'
        user.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            f'{user}\'s account has been approved.'
        )
        return redirect('account:user_requests')
    ctx = {
        'form': form,
    }
    return render(request, 'account/modify_approval.html', ctx)


@login_required
def permission_error(request):
    return HttpResponse('You don\'t have right permissio to access this page.')


@login_required(login_url='account_login')
def dashboard(request):
    total_students = Student.objects.count()
    total_teachers = Teacher.objects.count()
    total_departments = Department.objects.count()
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_departments': total_departments,
    }
    return render(request, 'dashboard.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password1'])
            new_user.save()
            auth_user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password1']
            )
            if auth_user is not None:
                login(request, auth_user)
            if auth_user.is_staff:
                return redirect('account:dashboard')
            else:
                return redirect('account:profile_complete')
        else:
            return render(request, 'account/register.html', {'user_form': user_form})

    else:
        user_form = UserRegistrationForm()
        return render(request, 'account/register.html', {'user_form': user_form})


class AccountListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = User
    template_name = 'academics/accounts_list.html'
    context_object_name = 'accounts'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('account:profile_complete')
        return redirect('account:login')



class GroupListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomGroup
    template_name = 'academics/group_list.html'
    context_object_name = 'groups'

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            return redirect('account:profile_complete')
        return redirect('account:login')


class UserRequestsListView(LoginRequiredMixin, ListView):
    queryset = User.objects.exclude(approval_status='a')
    template_name = 'account/user_requests.html'
    context_object_name = 'users'

user_requests_list = UserRequestsListView.as_view()