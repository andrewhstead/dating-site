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
from django.urls import include, path
from home import views as home_views
from users import views as user_views
from contacts import views as contact_views
from search import views as search_views
from staff import views as staff_views
from forum import views as forum_views
from django.contrib.flatpages import views

urlpatterns = [
    path(r'', home_views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('ajax/state_options/', user_views.state_options, name='state_options'),
    path('block/<int:profile>/', contact_views.block_user, name='block_user'),
    path('contact/', home_views.contact, name="contact"),
    path('favourite_user/<int:recipient>/', contact_views.favourite_user, name='favourite_user'),
    path('favourites/', contact_views.favourites, name='favourites'),
    path('favourites/added_me/', contact_views.favourited_me, name='favourited_me'),
    path('favourites/delete/<int:profile>/', contact_views.delete_favourite, name='delete_favourite'),
    path('favourites/mutual/', contact_views.mutual_favourites, name='mutual_favourites'),
    path('forum/', forum_views.forum_home, name='forum_home'),
    path('forum/<int:board_id>/', forum_views.board_home, name='board_home'),
    path('forum/<int:board_id>/new/', forum_views.new_thread, name='new_thread'),
    path('forum/activity/<int:user_id>/', forum_views.user_activity, name='user_activity'),
    path('forum/thread/<int:thread_id>/', forum_views.view_thread, name='view_thread'),
    path('forum/thread/<int:thread_id>/new/', forum_views.new_post, name='new_post'),
    path('forum/thread/<int:thread_id>/edit/<int:post_id>/', forum_views.edit_post, name='edit_post'),
    path('forum/thread/<int:thread_id>/delete/<int:post_id>/', forum_views.delete_post, name='delete_post'),
    path('login/', user_views.login, name="login"),
    path('logout/', user_views.logout, name="logout"),
    path('messages/', contact_views.all_messages, name='messages'),
    path('messages/<int:person_1>/<int:person_2>/', contact_views.message_thread, name='message_thread'),
    path('messages/new/<int:person_1>/<int:person_2>/', contact_views.new_thread, name='new_thread'),
    path('profile/', user_views.own_profile, name='own_profile'),
    path('profile/<int:user_id>/', user_views.view_profile, name='view_profile'),
    path('profile/edit/', user_views.user_profile, name='user_profile'),
    path('profile/delete/', user_views.delete_account, name='delete_account'),
    path('profile/password/', user_views.change_password, name='change_password'),
    path('register/', user_views.register, name='register'),
    path('search/', search_views.search_home, name="search_home"),
    path('search/results/<int:search_id>/', search_views.search_results, name="search_results"),
    path('staff/', staff_views.staff_home, name="staff_home"),
    path('support/', home_views.support, name="support"),
    path('support/<int:ticket_id>/', home_views.support_ticket, name='support_ticket'),
    path('support/new/', home_views.new_ticket, name="new_ticket"),
    path('views/', contact_views.profile_views, name='profile_views'),
    path('waved_at/<int:recipient>/', contact_views.waved_at, name='waved_at'),
    path('waves/', contact_views.waves, name='waves'),
    path('waves/sent/', contact_views.waves_sent, name='waves_sent'),
]

if settings.DEBUG is True:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls)), ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
