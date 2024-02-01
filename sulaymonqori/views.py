from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, CreateView, DetailView, DeleteView, UpdateView, ListView

from sulaymonqori.forms import RegistrationForm, PostCreateForm
from sulaymonqori.models import Post


class HomeView(View):
    def get(self, request):
        posts_for_homepage = Post.objects.order_by('-created_at')[:10]
        context = {
            "posts": posts_for_homepage,
        }

        return render(request, 'home.html', context=context)


class AboutView(TemplateView):
    template_name = 'about.html'


class PostDetailView(DetailView):
    template_name = "post_detail.html"
    model = Post
    context_object_name = "post"


class PostListView(ListView):
    model = Post
    template_name = 'user_posts.html'
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class PostCreateView(LoginRequiredMixin, CreateView):
    success_url = "blog:homepage"
    template_name = "post_create.html"
    success_message = "%(post) was published successfully"
    fields = ["title", "body"]


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "body"]
    success_url = "blog:homepage"
    template_name = "post_update.html"

    # success_message = "%(post) was updated successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("blog:homepage")
    template_name = "post_confirm_delete.html"


class RegisterView(View):
    # template_name = 'register.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'register.html', {'form': form})
