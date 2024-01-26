from django.urls import path , include
from . import views

urlpatterns = [
  
    path('', views.Home , name= 'Home'),
    path('addcards' , views.Addcards, name='addcards'),
    path('deletecard/<uuid:id>/', views.Deletecard , name='deletecard'),
    path('updatecard/<uuid:id>' , views.Updatecard, name='updatecard'  )

]