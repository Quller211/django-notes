
from django.shortcuts import render, redirect, get_object_or_404

from .models import Notes
from django.views.generic import ListView, UpdateView, CreateView
from .forms import FormNote, LoginForm, RegisterUser
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView, LogoutView



class NoteList(ListView):

    model = Notes
    template_name = 'main/list_of_notes.html'
    # allow_empty = False Запрещаем браузеру аоказывать пустой список из ListView

    # def get_queryset(self): Фильтруем вывод данных
    #     return Notes.objects.filter(...)
# =====================================================
# def notelist(request):
#     data = Notes.objects.all()

#     return render(request, 'main/list_of_notes.html', {'data': data})


def delete_note(request, notes_id):
    notes = Notes.objects.get(pk = notes_id)
    notes.delete()
    return redirect('list_of_notes')
    # Можно использоваьть DeleteView, но так как у нас всё меняется в пределах одной страницы, то оставить вопрос открытым


class CreateNote(CreateView):
    template_name = 'main/create_note.html'
    form_class = FormNote
    success_url = reverse_lazy('list_of_notes')
# ==================================================
# def create_note(request):
#     error_text = ""
#     if request.method == 'POST':
#         form = FormNote(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error_text += "Форма заполнена неправильно. Попробует ещё раз"
#     else:
#         form = FormNote()

#     return render(request, 'main/create_note.html', {'form': form, 'error_text': error_text})


class Edit_Note(UpdateView):
    model = Notes
    template_name = 'main/to_edit.html'
    form_class = FormNote
    success_url = reverse_lazy('list_of_notes')

class LoginUser(LoginView):
    form_class = LoginForm
    template_name = 'main/start.html'
    next_page = 'list_of_notes' # Вместо get_success_url

class LogoutUser(LogoutView):
    next_page = 'start'

# def logout_user(request):
#     logout(request)
#     return redirect('start')

class Register(CreateView):
    form_class = RegisterUser
    template_name = 'main/register.html'
    success_url = reverse_lazy('start')


