from django.urls import path
from .views import Home, ProfileList, ProfileCreate, Watch

app_name = "core"


urlpatterns = [
    # URL path for Home page
    path("", Home.as_view()),
    # URL path for ProfileList
    path("profile/", ProfileList.as_view(), name="profile_list"),
    # URL path for ProfileCreate
    path("profile/create/", ProfileCreate.as_view(), name="profile_create"),
    # URL path for MovieList
    path("watch/<uuid:profile_id>/", Watch.as_view(), name="watch"),
]
