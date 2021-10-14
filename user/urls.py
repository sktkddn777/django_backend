from django.urls import path


from .views import index, home, signup, login, logout

app_name = 'user'

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),

    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
]