from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from todolist import models as django_models
from .forms import PostForm

from .models import ToDo, Post


# Create your views here.


def index(request):
    todos = ToDo.objects.all()
    return render(request, 'todoapp/index.html', {'todo_list': todos, 'title': 'Главная страница'})


@require_http_methods(['POST'])
@csrf_exempt
def add(request):
    title = request.POST['title']
    todo = ToDo(title=title)
    todo.save()
    return redirect('index')


def update(request, todo_id):
    todo = ToDo.objects.get(id=todo_id)
    todo.is_complete = not todo.is_complete
    todo.save()

    return redirect('index')


def test(request):
    return render(request, "todoapp/contacts.html", {'title': 'Контакты'})


def delete(request, todo_id):
    django_models.ToDo.objects.filter(id=todo_id).delete()

    return redirect('index')


class DeletePostView(ListView):
    model = Post.delete
    template_name = 'todoapp/home.html'
    success_url = reverse_lazy('home')


def task_v(request):
    return render(request, "todoapp/create_task.html", {'Task': 'Task'})


class HomePageView(ListView):
    model = Post
    template_name = 'todoapp/home.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'todoapp/post_create.html'
    success_url = reverse_lazy('home')


# class DetailPostView(ListView):
#     model = Post
#     form_class = PostForm
#     template_name = 'todoapp/more_task_post.html'
#     success_url = reverse_lazy('detail')


def more_button(request):
    return render(request, "todoapp/more_task_post.html")


# class DetailToDoView(ListView):
#     model = ToDo
#     template_name = 'todoapp/more_task_post_2.html'
#     success_url = reverse_lazy('detail_2')


def detail_POST(request, slug):
    template_name = "todoapp/post.html"
    post = get_object_or_404(Post, slug=slug)
    return render(
        request,
        template_name,
        {
            "post": post,
        },
    )


def detail_TODO(request, todo_id):
    django_models.ToDo.objects.all()
    django_models.ToDo.objects.filter(id=todo_id).order_by('-id')

    return render(request, 'todoapp/more_task_post_2.html', {'detail': 'detail'})


class ContactListView(ListView):
    paginate_by = 2
    model = ToDo


def listing(request):
    contact_list = ToDo.objects.all()
    paginator = Paginator(contact_list, 25)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_obj': page_obj})


def main(request):
    return render(request, 'todoapp/main.html')
