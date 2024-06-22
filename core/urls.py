from django.urls import path
from . import views
urlpatterns = [
    # Na pagina inical que o usuario vai colocar o link escolhido e o link que será encurtado
    path('', views.home, name='home'),
    path('valida_link/', views.valida_link, name='valida_link'),
    path('<str:link>', views.redirecionar, name='redirecionar')

]
