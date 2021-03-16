from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from smarthome.models import Task
from .models import Topic

num_books = 0


def update():
    global num_books
    num_books = Task.objects.filter(is_performed=False).count()


@login_required
def record_log(request):
    update()
    topics = Topic.objects.order_by('-date_added')
    context = {
        'topics': topics,
        'num_books': num_books,

    }
    return render(request,
                  'logs/index.html', context)


@login_required
def topic(request, topic_id):
    update()
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {
        'topic': topic,
        'entries': entries,
        'num_books': num_books,

    }
    return render(request,
                  'logs/topic.html', context)
