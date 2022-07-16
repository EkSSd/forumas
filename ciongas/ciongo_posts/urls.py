from django.urls import path
from django.contrib.admin.views.decorators import staff_member_required
from . import views
from .views import (
    HomeView,
    BlogView,
    TagView,
    AddPostView,
    UpdatePostView,
    AddTaggView,
    UserListView,
    AllTaggView,
  
    )

urlpatterns = [
    # path('/', views.home, name = 'blog-home'),
    path('', HomeView.as_view(), name="home"),
    path('authors/',UserListView.as_view(), name='authors'),
    path('authors/<int:author_id>', views.author, name = 'author'),
    path('article/<int:pk>', views.BlogView.as_view(), name = "blog"),
    path('tags/<int:pk>', TagView.as_view(), name = "tag"),
    path('article/', AddPostView.as_view(), name = 'addpost'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('delete/<post_id>',views.delete_post,name='delete'),
    path('addtag/', staff_member_required(AddTaggView.as_view()), name = 'addtag'),
    path('all_tags/', AllTaggView.as_view(), name = "all_tags"),
    path('delete_tag/<int:tag_id>',views.delete_tag,name='delete_tag'),
]