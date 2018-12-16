from django.urls import path

from . import views

urlpatterns = [
    path('base', views.base_view, name='base'),
    path('', views.index_view, name='index'),
    path('question/<int:question_id>', views.question_view, name='question'),
    path('ask', views.ask_view, name='ask'),
    path('login', views.login_view, name='login'),
    path('signup', views.signup_view, name='signup'),
    path('settings', views.settings_view, name='settings'),
    path('hot', views.hot_view, name='hot'),
    path('tag/<tag_text>', views.tag_view, name='tag'),
    path('logout', views.logout, name='logout')
]