from django.urls import path


from .views import home, signup, login, logout

urlpatterns = [
    path('home/', home, name='home'),

    path('home/signup/', signup, name='signup'),
    path('home/login/', login, name='login'),
    path('home/logout/', logout, name='logout'),
]