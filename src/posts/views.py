from django.urls import reverse, reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import JsonResponse,HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from posts.models import Post, Comment
from .form import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class Index(LoginRequiredMixin, ListView):
    login_url = '/user/'
    redirect_field_name = ''
    template_name = "index.html"
    model = Post
    context_object_name = 'posts'
    paginate_by = 5
    ordering = ("-timestamp")


class CreatePost(SuccessMessageMixin ,CreateView):
    template_name = "form/form_post.html"
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('home')
    success_message = "%(title)s fue creado correctamente"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.title,
        )


class DetailPost(LoginRequiredMixin, DetailView):
    login_url = '/user/'
    redirect_field_name = ''
    template_name = "detail.html"
    model = Post

    def get_context_data(self, *args, **kwargs):
        obj = self.object.id
        context = super(DetailPost, self).get_context_data(*args, **kwargs)
        context['comments'] = Comment.objects.filter(post= obj)
        print(context['comments'])
        return context


class UpdatePost(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = '/user/'
    redirect_field_name = ''
    template_name = "form/form_post.html"
    model = Post
    form_class = PostForm
    success_message = "%(title)s fue modificado correctamente"
    success_url = reverse_lazy('home')


    def get_context_data(self, *args, **kwargs):
        context = super(UpdatePost, self).get_context_data(*args, **kwargs)
        context['update'] = True
        return context


class DeletePost(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = '/user/'
    redirect_field_name = ''
    model = Post
    template_name = 'delete.html'
    success_message = "%(title)s  fue eliminado correctamente"
    success_url = reverse_lazy('home')


    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(request, self.success_message % dict(title = obj))
        return super(DeletePost, self).delete(request, *args, **kwargs)

def create_comment(request):
    if request.method == "POST":
        data = request.POST
        autor = str(data.get('autor',''))
        content = str(data.get('content'))
        id = data.get('id')
        post = Post.objects.get(id=id)
        Comment.objects.create(autor=request.user.username , content= content, post = post)
        comments = serializers.serialize('json',Comment.objects.filter(post=id))
    return HttpResponse(comments)

