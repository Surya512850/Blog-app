from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView, CreateView,UpdateView,DeleteView
from .models import Post, PreviousPost
from .forms import PostForm,EditForm, PrevUpdateForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']

class ArticleView(DetailView):
    model = Post
    template_name = 'details.html'

class PreviousView(DetailView):
    model = PreviousPost
    template_name = 'prev_details.html'

def previous_update(request, pk):
    post = PreviousPost.objects.get(pk = pk)
    form = PrevUpdateForm(request.POST or None, instance = post)
    if form.is_valid():
        form.instance.author = request.user
        form.save()
        orig_post = post.post
        orig_post.title = form.instance.title
        orig_post.body = form.instance.body
        orig_post.save()
        return redirect("home")
    context = {"object":post,"form":form}
    return render(request,"prev_update.html",context)

class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create-blog.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        new_post = form.save()
        obj = PreviousPost(author = new_post.author,post=new_post,title = new_post.title, body = new_post.body)
        obj.save()
        return super().form_valid(form)

class UpdatePost(UpdateView):
    model = Post
    template_name = 'update.html'
    form_class = EditForm
    def form_valid(self,form):
        form.instance.author = self.request.user
        updated = form.save()
        obj = PreviousPost(author = updated.author, post = updated, title = updated.title, body = updated.body)
        obj.save()
        return super().form_valid(form)
    

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class UserPosts(ListView):
    model = Post
    template_name = 'user_posts.html'
    def get_queryset(self):
        return Post.objects.filter(author = self.request.user).order_by('-date')

def previous_posts(request,pk):
    obj = Post.objects.get(pk = pk)
    posts = PreviousPost.objects.filter(post = obj).order_by("-date")
    context = {'object_list':posts}
    return render(request,'previous.html',context)

