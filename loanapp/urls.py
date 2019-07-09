from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from core import views as core_views
from core.views import Signup,Index,Show
urlpatterns = [
    path('', core_views.home, name='home'),
    path('login', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('Signup', Signup.as_view(), name='Signup'),
    path('index/', Index.as_view(),name='Index'),
    path('show/', Show.as_view(), name='show')

]