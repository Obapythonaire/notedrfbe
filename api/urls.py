from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('notes', views.Notes, name='notes'),
    # path('notes/create/', views.createNote, name='create-note'),
    # path('notes/<str:pk>/update/', views.updateNote, name='note-update'),
    # path('notes/<str:pk>/delete/', views.DeleteNote, name='note-delete'),



    path('notes/<str:pk>/', views.getNote, name='note'),
    
]