from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',user_logIn,name="login"),
    path('employee/register',employee_registration, name='employee-registration'),
    path('employer/register',employer_registration, name='employer-registration'),
    path('profile/edit/<int:id>/', employee_edit_profile, name='edit-profile'),
    path('logout/', user_logOut, name='logout'),
    path('', include('jobapp.urls')),
    path('cvbuilder/', include('cvbuilder.urls')),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)