from django.shortcuts import render,redirect,get_object_or_404
from .models import Task


# Create your views here.

def add_task(request):
    if request.method=='POST':
        title=request.POST.get('title')
        if title:
            Task.objects.create(title=title)
    return redirect('task_list')
def toggle_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.done = not task.done
    task.save()
    return redirect('task_list')
def delete_task(request,pk):
    task =  get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('task_list')
def task_list(request):
    tasks = Task.objects.all().order_by('-created_at')
    done_count = tasks.filter(done=True).count()
    pending_count = tasks.filter(done=False).count()
    progress = round((done_count / tasks.count() * 100) if tasks.count() > 0 else 0)
    return render(request, 'tasks/index.html', {
        'tasks': tasks,
        'done_count': done_count,
        'pending_count': pending_count,
        'progress': progress,
    })