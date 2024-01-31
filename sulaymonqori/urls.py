from django.urls import path

from sulaymonqori.views import HomeView

appname = "blog"
urlpatterns = [
    path('', HomeView.as_view(), name="homepage"),
]
