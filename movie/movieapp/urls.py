
from django.urls import path, include
from movieapp import views
app_name='movieapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('film/<int:movieid>/',views.details,name='details'),
    path('add/',views.add,name='add'),
    path('updated/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]