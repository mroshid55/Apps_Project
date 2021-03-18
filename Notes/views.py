from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
from .forms import *
from .models import *


@login_required(login_url='Login')
def NOTES(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user).order_by('-id')
        form = NotesForm()
        if request.method == 'POST':
            form = NotesForm(request.POST)
            if form.is_valid():
                form.instance.user = request.user
                form.save()
                return redirect('Notes')
            else:
                form = NotesForm()
        context = {'notes': notes, 'form': form}
        return render(request, "Notes/apps_notes.html", context)
    else:
        return render(request, "Accounts/Login.html")


def UPDATE_NOTES(request, pk):
    edit_note = Note.objects.get(id=pk)
    form = NotesForm(instance=edit_note)
    if request.method == 'POST':
        form = NotesForm(request.POST, instance=edit_note)
        if form.is_valid():
            form.save()
            return redirect('Notes')

    context = {'form': form}
    return render(request, "Notes/apps_notes_update.html", context)


def DELETE_NOTES(request, pk):
    delete_note = Note.objects.get(id=pk)
    if request.method == 'POST':
        delete_note.delete()
        return redirect('Notes')
    context = {'delete_note': delete_note}
    return render(request, 'Notes/apps_notes_delete.html', context)
