from django.urls import path
# from .views import home 
from .views import HomeView, BlogDetailView

urlpatterns = [
    # path('', home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="blog_detail"),
]

