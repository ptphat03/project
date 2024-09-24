from django.shortcuts import render,redirect, get_object_or_404
from .models import TestGroup, Test
from .forms import TestGroupForm, TestForm

def test_group_list(request):
    test_groups = TestGroup.objects.all()
    return render(request, 'test_group_list.html', {'test_groups' : test_groups})

def test_group_detail(request, pk):
    test_group = get_object_or_404(TestGroup, pk=pk)
    return render(request, 'test_group_detail.html', {'test_group': test_group})

def test_group_add(request):
    if request.method == 'POST':
        form = TestGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_group:test_group_list')
    else:
        form = TestGroupForm()
    return render(request, 'test_group_form.html', {'form': form})

def test_group_edit(request, pk):
    test_group = get_object_or_404(TestGroup, pk=pk)
    if request.method == 'POST':
        form = TestGroupForm(request.POST, instance=test_group)
        if form.is_valid():
            form.save()
            return redirect('test_group:test_group_list')
    else:
        form = TestGroupForm(instance=test_group)
    return render(request, 'test_group_form.html', {'form': form})

def test_group_delete(request, pk):
    test_group = get_object_or_404(TestGroup, pk=pk)
    if request.method == 'POST':
        test_group.delete()
        return redirect('test_group:test_group_list')
    return render(request, 'test_group_confirm_delete.html', {'test_group': test_group})

def test_list(request):
    tests = Test.objects.all()
    return render(request, 'test_list.html', {'tests' : tests})

def test_detail(request, pk):
    test = get_object_or_404(Test, pk=pk)
    return render(request, 'test_detail.html', {'test': test})

def test_add(request):
    if request.method == 'POST':
        form = TestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('test_group:test_list')
    else:
        form = TestForm()
    return render(request, 'test_form.html', {'form': form})

def test_edit(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        form = TestForm(request.POST, instance=test)
        if form.is_valid():
            form.save()
            return redirect('test_group:test_list')
    else:
        form = TestForm(instance=test)
    return render(request, 'test_form.html', {'form': form})

def test_delete(request, pk):
    test = get_object_or_404(Test, pk=pk)
    if request.method == 'POST':
        test.delete()
        return redirect('test_group:test_list')
    return render(request, 'test_confirm_delete.html', {'test': test})