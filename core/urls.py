from django.urls import path
from .views import Home, ProfileList  # import Home view

app_name = "core"

# set url path for Home page
urlpatterns = [
    path("", Home.as_view()),
    # URL path for ProfileList
    path("profile/", ProfileList.as_view(), name="profile_list"),
]
