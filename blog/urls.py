from . import views
from django.urls import path
from .views import get_queryset, error404_page

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('error404_page/', views.error404_page, name='404'),
    path('error505_page/', views.error505_page, name='505'),
    path('search/', views.get_queryset, name='get_queryset'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
