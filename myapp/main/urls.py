from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('addnews/', views.add_news_page, name='add_news'),
    path('news/', views.news_page, name='news_page'),
    path('search/', views.search_page, name='search_page'),
    path('read/', views.read_page, name='read_page')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
