from django.urls import path
from . import views
from .views import HomeView, BlogView, TagView, AddPostView

urlpatterns = [
    # path('/', views.home, name = 'blog-home'),
    path('', HomeView.as_view(), name="home"),
    path('authors/',views.authors, name='authors'),
    path('authors/<int:author_id>', views.author, name = 'author'),
    path('article/<int:pk>', BlogView.as_view(), name = "blog"),
    path('tags/<int:pk>', TagView.as_view(), name = "tagg"),
    path('addpost/', AddPostView.as_view(), name = 'addpost'),
]