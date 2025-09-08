from django.urls import path
from .views import Home, ProfileList, ProfileCreate, Watch, ShowMovieDetail, ShowMovie

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
    # URL path for MovieDetail
    path("movie/detail/<str:movie_id>/", ShowMovieDetail.as_view(), name="show_detail"),
    # URL path for ShowDetail
    path("movie/play/<str:movie_id>/", ShowMovie.as_view(), name="play"),
]
