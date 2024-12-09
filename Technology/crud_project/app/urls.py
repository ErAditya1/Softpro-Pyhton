
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', home , name='home'),
    path('save/', saveInfo, name='save'),
    path('edit/', editInfo, name='edit'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),



]