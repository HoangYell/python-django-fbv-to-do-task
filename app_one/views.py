from django.shortcuts import render, get_object_or_404
from app_one.models import Task
from app_one.forms import TaskForm
# Create your views here.


def task_list(request):
    # if request.method == "GET":
    #     pass
    tasks = Task.objects.all()
    data = {'task_list': tasks}
    return render(request, 'app_one/task_list.html', data)


def update_task(request, pk=None):
    task_form = TaskForm()
    if pk:
        # task = get_object_or_404(Task, pk=pk)
        task = Task.objects.get(pk=pk)
        task_form = TaskForm(instance=task)
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.pk = pk
            task.save()
            return task_list(request)
        else:
            print("Error Form Invalid")
    return render(request, 'app_one/task_form.html', {'form': task_form})


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return task_list(request)
