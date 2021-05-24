from django.urls import path

from . import views

urlpatterns = [
       
	path('', views.loja, name="loja"),
	path('carrinho/', views.carrinho, name="carrinho"),
	path('escapar/', views.escapar, name="escapar"),

]