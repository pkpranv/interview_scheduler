from django.urls import path
#
from .views.users import RegistrationView,LoginView
from .views.availablity import UpdateAvailablity,GetAvailablity

urlpatterns = [
    path('register/', RegistrationView.as_view(),
         name='register'),
    path('login/', LoginView.as_view(),
         name='login'),
    path('update_availablity/', UpdateAvailablity.as_view(),
         name='update_availablity'),
    path('get_availablity/', GetAvailablity.as_view(),
         name='get_availablity')
    ]