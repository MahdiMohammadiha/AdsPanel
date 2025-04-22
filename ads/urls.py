from django.urls import path
from .views import index, AdList, AdDetail

urlpatterns = [
    # Upload image template temporary disabled
    # path("", index, name="index"),
    
    path("list/", AdList.as_view()),

    # Read notes in todo.md
    # path("api/ad/<int:pk>/", AdDetail.as_view()),  
]
