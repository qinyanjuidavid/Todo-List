from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from myapp.models import Todo
from myapp.forms import TodoForm,DoneForm
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    todo_obj=Todo.objects.all().order_by('-time_added','-time_updated')
    if request.method=="POST":
        todoform=TodoForm(request.POST or None, request.FILES or None)
        sucform=DoneForm(request.POST or None,request.FILES or None)
        if todoform.is_valid() and suform.is_valid():
            todoform.save(commit=True)
            todoform=TodoForm()
            sucform.save()
    else:
        todoform=TodoForm()
        sucform=DoneForm()
    context={
    'todo':todo_obj,
    'form':todoform,
    'sucform':sucform
    }
    return render(request,'myapp/home.html',context)
def Registration(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            obj=form.save(commit=False)
            obj.save()
            form=UserCreationForm()
    else:
        form=UserCreationForm()
    context={
    'form':form
    }
    return render(request,'myapp/register.html',context)
@login_required
def delete(request,id):
    instance=Todo.objects.get(id=id)
    instance.delete()
    return HttpResponseRedirect('/home/')
@login_required
def update(request,id):
    instance=Todo.objects.get(id=id)
    form=TodoForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance.save()
        return HttpResponseRedirect('/home/')
    context={
    'form':form
    }
    return render(request,'myapp/update.html',context)
