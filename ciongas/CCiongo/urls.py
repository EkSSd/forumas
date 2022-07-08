from django.urls import path
from . import views
from .views import (
    HomeView,
    BlogView,
    TagView,
    AddPostView,
    UpdatePostView,
    
    )

urlpatterns = [
    # path('/', views.home, name = 'blog-home'),
    path('', HomeView.as_view(), name="home"),
    path('authors/',views.authors, name='authors'),
    path('authors/<int:author_id>', views.author, name = 'author'),
    path('article/<int:pk>', BlogView.as_view(), name = "blog"),
    path('tags/<int:pk>', TagView.as_view(), name = "tagg"),
    path('article/', AddPostView.as_view(), name = 'addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete/<post_id>',views.delete_post,name='delete'),
]