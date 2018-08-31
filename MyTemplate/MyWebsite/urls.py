from django.urls import path

from . import views
urlpatterns = [
    path('',views.MainPageView.as_view(),name='index'),
    path('about/',views.aboutPageView.as_view(),name='about'),
    path('contact/',views.ContactPageView.as_view(),name='contact'),
]
