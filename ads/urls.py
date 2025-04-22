from django.urls import path
from .views import index, AdList, AdDetail

urlpatterns = [
    path("", index, name="index"),
    path("api/ad/", AdList.as_view()),

    # Read notes in todo.md
    # path("api/ad/<int:pk>/", AdDetail.as_view()),  
]
