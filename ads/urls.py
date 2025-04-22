from django.urls import path
from .views import index, AdList, AdDetail, AdsByService

urlpatterns = [
    # Upload image template temporary disabled
    # path("", index, name="index"),
    
    path("list/", AdList.as_view(), name="ads-list"),
    path("list/<int:service_id>/", AdsByService.as_view(), name="ads-by-service"),

    # Read notes in todo.md
    # path("api/ad/<int:pk>/", AdDetail.as_view()),
]
