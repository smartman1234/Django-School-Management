from django.forms import ModelForm
from .models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'date_of_birth',
                  'designation', 'expertise',
                  'mobile', 'email', ]
