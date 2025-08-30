from django.urls import path
from .views import Home  # import Home view

app_name = "core"

# set url path for Home page
urlpatterns = [path("", Home.as_view())]
