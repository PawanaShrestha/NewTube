from django.urls import path
from .import views

# from newtubeapp.views import VideoView

urlpatterns = [
    path('', views.HomeView, name = "home"),
    path('upload_new_video/', views.upload_new_video, name = 'upload-new-video'),
    path('search_videos/', views.search_videos, name = 'search-videos'),
    path('update_post/<post_id>', views.update_post, name = "update-post"),
    path('delete_post/<post_id>', views.delete_post, name = "delete-post"),
    path('video/<post_id>/', views.play_video, name = "play-video-view"),
    path('users_profile/<user_name>/', views.users_profile, name = "users_profile"),
]

