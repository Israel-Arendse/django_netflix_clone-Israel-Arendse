from django.shortcuts import render
from django.views import View

# Import login_requred and method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Home view
class Home(View):  # class for inheriting 'home' view
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")


# Profile view
@method_decorator(login_required, name="dispatch")
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request, "profileList.html", {"profiles": profiles})
