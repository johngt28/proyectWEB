from django.urls import path 
from .views import index
from .views import Artistas
from .views import galeria
from .views import log_in
from .views import perfil_art
from .views import registro


urlpatterns =[
    path('',index,name="index"),
]

urlpatterns =[
    path('',Artistas,name="Artistas"),
]

urlpatterns =[
    path('',galeria,name="galeria"),
]

urlpatterns =[
    path('',log_in,name="log_in"),
]

urlpatterns =[
    path('',perfil_art,name="perfil_art"),
]

urlpatterns =[
    path('',registro,name="registro"),
]