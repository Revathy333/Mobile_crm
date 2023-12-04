"""
URL configuration for employee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from work.views import EmpView, BookView, MoviesView, MovieList, FacultyView, FacultyList,MovieDetailView
from work.views import MobilesView,MobileDetailView, MobileGetOne, StudentNewView, StudentList,MobileDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('model1/',EmpView.as_view()),
    path('book/', BookView.as_view()),
    path('movie/',MoviesView.as_view()),
    path('book/all',MovieList.as_view()),
    path('faculty/', FacultyView.as_view()),
    path('faculty/all',FacultyList.as_view()),
    path('book/<int:pk>',MovieDetailView.as_view()),
    path('mobile/', MobilesView.as_view()),
    path('mobile/all',MobileDetailView.as_view(),name='mobile-all'),
    path('mobile/<int:pk>',MobileGetOne.as_view(),name='mobile-new'),
    path('student/',StudentNewView.as_view()),
    path('student/all',StudentList.as_view()),
    path('mobile/<int:pk>/remove',MobileDelete.as_view(),name='mobile-delete')
]
