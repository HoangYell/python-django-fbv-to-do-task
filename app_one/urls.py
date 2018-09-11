from django.conf.urls import url
from app_one import views


app_name = 'app_one'

urlpatterns = [
    url(r'^$', views.task_list, name='task_list'),
    url(r'^task/new/$', views.update_task, name='update_task'),
    url(r'^task/update/(?P<pk>\d+)/$', views.update_task, name='update_task'),
    url(r'^task/delete/(?P<pk>\d+)/$', views.delete_task, name='delete_task'),
]
