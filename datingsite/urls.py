"""datingsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from home import views as home_views
from users import views as user_views

urlpatterns = [
    path(r'', home_views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('login/', user_views.login, name="login"),
    path('logout/', user_views.logout, name="logout"),
    path('profile/<int:user_id>/', user_views.view_profile, name='view_profile'),
    path('profile/edit/', user_views.user_profile, name='user_profile'),
    path('profile/delete/', user_views.delete_account, name='delete_account'),
    path('profile/password/', user_views.change_password, name='change_password'),
    path('register/', user_views.register, name='register'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
