from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.getNotes, name="notes"),
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name="login"),
    path('hide/', views.hide, name="hide"),
    path('unhide/', views.unhide, name="unhide"),
    
    # path('notes/create/', views.createNote, name="create-note"),
    #path('notes/<str:pk>/update/', views.updateNote, name="update-note"),
    #path('notes/<str:pk>/delete/', views.deleteNote, name="delete-note"),

    path('notes/<str:pk>/', views.getNote, name="note"),
]
