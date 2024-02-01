from django.urls import path

from sulaymonqori.views import HomeView, PostDetailView, RegisterView, PostUpdateView, PostDeleteView, PostCreateView, \
    PostListView, AboutView

app_name = "blog"
urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
    path('about/', AboutView.as_view(), name="about"),

    path('register/', RegisterView.as_view(), name='register'),
    path('post/', PostListView.as_view(), name='post_list'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
]
