from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('posts/', views.posts),
    path('post/<int:post_id>/', views.post_one),
    path('posts/category/<int:category_id>', views.post_cat)
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)
