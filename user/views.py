from django.shortcuts import render,redirect, get_object_or_404
from .models import User
from .forms import UserForm

# Create your views here.
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users' : users})

def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})

def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:user_list')
        else:
            # If form is invalid, print form errors to debug
            print(form.errors)  # Optional, useful for debugging
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def user_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'user_form.html', {'form': form})

def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user:user_list')
    return render(request, 'user_confirm_delete.html', {'user': user})