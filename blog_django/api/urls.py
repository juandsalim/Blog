from django.urls import path
from .views import miembroView


#lista 
urlpatterns = [
    path('Miembro/',miembroView.as_view(),name ='miembros_list'),
    path('Miembro/<int:id>',miembroView.as_view(),name ='miembros_process')
]