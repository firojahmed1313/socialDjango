from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('',views.socialListView,name='socialListView'),
    path('create/',views.socialCreateView,name='socialCreateView'),
    path('<int:pk>/update/',views.socialUpdateView,name='socialUpdateView'),
    path('<int:pk>/delete/',views.socialDeleteView,name='socialDeleteView'),
]