from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'app_post'

urlpatterns = [
    path('', views.homePage, name='home'),
    path('<int:pk>', views.post, name='post'),
    path('blogs', views.blog, name='blogs'),
    path('contact', views.contact, name='contact'),
]
urlpatterns += staticfiles_urlpatterns()



