from django.urls import path
from . import views

urlpatterns = [
    path('',views.view, name='view'),
    path('index/',views.index, name='index'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path("delete/<int:id>", views.delete, name="deletedata"),
]