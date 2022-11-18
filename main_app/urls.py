from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete_widget/<int:widget_id>', views.delete_widget, name="delete_widget")

]