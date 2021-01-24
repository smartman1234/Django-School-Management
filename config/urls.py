from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts.views import dashboard


admin.site.site_header = "SMS-LIO Admin"
admin.site.site_title = "SMS-LIO Admin Portal"
admin.site.index_title = "Welcome to SMS-LIO Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('dashboard/', dashboard, name='index_view'),
    path('accounts/', include('allauth.urls')),
    path('blog/', include('articles.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('account/', include('accounts.urls')),
    path('academics/', include('academics.urls')),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
    path('result/', include('result.urls')),
    path('password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='account/password/password_reset.html'
        ),
        name="password_reset",
    ),
    path('password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='account/password/password_reset_done.html'
        ),
        name="password_reset_done",
    ),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='account/password/password_reset_confirm.html'
        ),
        name='password_reset_confirm',
    ),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='account/password/password-reset-complete.html'
        ),
    name='password_reset_complete'
    ),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)

if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls))
        ] + urlpatterns
