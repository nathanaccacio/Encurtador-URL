from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #Cria um redirecionamento para o core.urls
    path('', include('core.urls'))
]
