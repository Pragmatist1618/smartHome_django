from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponse, JsonResponse
from django.shortcuts import render

from .models import Task
from gpio.models import GPIO

num_books = 0


def update():
    global num_books
    num_books = Task.objects.filter(is_performed=False).count()


@login_required
def index(request):
    update()
    gpios = GPIO.objects.all()
    gpio_state = {}
    for gpio in gpios:
        gpio_state[gpio.name] = {'num': gpio.num, 'state': gpio.state}
    #print(gpio_state)
    context = {
        'num_books': num_books,
        'gpio_state': gpio_state,

    }
    return render(request,
                  'smarthome/index.html', context)


@login_required
def tasks(request):
    update()
    tasks = Task.objects.filter(is_performed=False).order_by('-date_added')

    context = {
        'num_books': num_books,
        'tasks': tasks,

    }
    return render(request,
                  'smarthome/tasks.html', context)


@login_required
def performed(request, id):
    try:
        task = Task.objects.get(id=id)
        task.is_performed = True
        task.save()
        return HttpResponseRedirect('/tasks/')
    except Task.DoesNotExist:
        return HttpResponseNotFound("<h2>Tasks not found!</h2>")


@login_required
def add_task(request):
    if request.method == "POST":
        task = Task()
        task.text = request.POST.get("text")
        task.user = request.user
        task.save()
    return HttpResponseRedirect("/tasks/")


def change_gpio(request):
    if request.method == "POST":
        try:
            name = request.POST['name'] + '_gpio'
            gpio = GPIO.objects.get(name=name)
            gpio.state = request.POST['state']
            gpio.save()
        except GPIO.DoesNotExist:
            print('change_gpio error')
    return HttpResponse()


def state_gpio(request):
    if request.method == "GET":
        try:
            data = {}
            gpios = GPIO.objects.all()
            for gpio in gpios:
                data[gpio.name] = gpio.state
        except GPIO.DoesNotExist:
            print('state_gpio error')
    return JsonResponse(data)
