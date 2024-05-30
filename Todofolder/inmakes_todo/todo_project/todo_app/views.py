from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from. models import tasks1
from.forms import Todoform
from django.views.generic import ListView, DetailView, UpdateView, DeleteView


# Create your views here.
class Tasklistview(ListView):
     model = tasks1
     template_name = 'add.html'
     context_object_name = 'Task'
class Taskdetailview(DetailView):
    model = tasks1
    template_name = 'detail1.html'
    context_object_name = 'task'
class Taskupdateview(UpdateView):
    model = tasks1
    template_name = 'update1.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cvedetail',kwargs={'pk':self.object.id})
class Taskdeleteview(DeleteView):
    model = tasks1
    template_name = 'delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('cbvhome')







def add(request):
    task1 = tasks1.objects.all()
    if request.method == 'POST':
        name=request.POST.get('task','')
        Priority = request.POST.get('priority','')
        date = request.POST.get('date','')
        Task=tasks1(name=name,priority=Priority,date=date)
        Task.save()
        return redirect('/')
    return render(request,'add.html',{'task':task1})

def detail(request,taskid):
    Task=tasks1.objects.get(id=taskid)
    if request.method == 'POST':
        Task.delete()
        return redirect('/')
    return render(request,'detail1.html')
def update(request,id):
    task=tasks1.objects.get(id=id)
    f=Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'update.html',{'f':f,'task':task })
