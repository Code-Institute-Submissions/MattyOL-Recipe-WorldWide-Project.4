from . import views
from django.urls import path
from .views import SearchResultsView, error404_page

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('error404_page/', views.error404_page, name='404'),
    path('error505_page/', views.error505_page, name='505'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
