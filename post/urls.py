
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('first_http/', views.http_responce),
    path('post_list/', views.post_list_api_view),
    path('post_list/<int:post_id>/', views.post_detail_api_view),
    path('', views.first_render),
    path('create_post/', views.create_post_view),
    path('create_category/', views.create_category_view),
    path('create_tag/', views.create_tag_view),
    path('posts/<int:post_id>/create_review/', views.create_comment_view, name='create_review'),

]
