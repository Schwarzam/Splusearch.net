"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as users_views
from search import views as search_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home Page #
    path('', include('index.urls')),

    ## SearchBy
    path('searchby/', search_views.searchby, name='searchby'),
    path('searchcoords/', search_views.searchcoords, name='searchcoords'),
    path('searchid/', search_views.searchid, name='searchid'),
    path('upload/', search_views.upload, name='upload'),

    ## Saving/Delete and Profile search
    path('searchid/save', search_views.save, name ='save'),
    path('^searchfromprof/save', search_views.save, name ='save'),
    path('searchcoords/save', search_views.save, name ='save'),
    path('upload/save', search_views.save, name ='save'),
    path('profile/delete', search_views.delete, name ='delete'),
    path(r'^searchfromprof/searchfromprof-(?P<param>[\w-]+).html', search_views.searchfromprof, name="searchfromprof"),

    # Profile
    path('profile/', users_views.profile, name='profile'),

    ## Register and Login ##
    path('register/', users_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
