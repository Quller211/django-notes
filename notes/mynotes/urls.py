from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginUser.as_view(), name = 'start'),
    path('exit/', views.LogoutUser.as_view(), name = 'exit'),
    path('register', views.Register.as_view(), name = 'register'),
    path('list_of_notes', views.NoteList.as_view(), name = 'list_of_notes'),
    path('delete_note/<notes_id>', views.delete_note, name = 'delete-note'),
    path('to_create', views.CreateNote.as_view(), name = 'create-note'),
    path('to_edit/<int:pk>', views.Edit_Note.as_view(), name = 'to-edit')
]
