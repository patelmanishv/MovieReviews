from django.urls import path
from movie import views as movieViews 

urlpatterns = [
    path('', movieViews.home, name='home'),
    path('about/', movieViews.about, name='about'),
    path('signup/', movieViews.signup, name='signup'),
]