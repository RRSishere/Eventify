from django.contrib import admin
from django.urls import path
from eventify import views

from django.conf import settings
from django.conf.urls.static import static


from .views import scrape_links, TaskList, TaskCreate
from. import views



urlpatterns = [
    # Your existing URL patterns
    path('admin/', admin.site.urls),
    path('', views.page),
    path('contactus/', views.contactus, name='contactus'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('scrape-links/', scrape_links, name='scrape_links'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('logout/', views.logout_view, name='logout'),
    path('task-list/',TaskList.as_view(), name='tasks'),
    path('create-task/',TaskCreate.as_view(), name='task-create')
]