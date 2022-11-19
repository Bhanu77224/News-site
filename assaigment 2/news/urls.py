from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name="home"),
    path('business',views.business,name="n_business"),
    path('sports',views.sports,name="n_sports"),
    path('Entertainment',views.Entertainment,name="n_Entertainment"),
    path('Science',views.Science,name="n_Science"),
    path('Automobile',views.Automobile,name="n_Automobile"),
    path('startup',views.startup,name="n_startup"),
    path('Politics',views.Politics,name="n_Politics"),

]
