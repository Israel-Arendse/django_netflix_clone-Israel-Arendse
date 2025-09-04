from django.shortcuts import redirect, render
from django.views import View

# Import login_requred and method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Import from core/forms.py
from .forms import ProfileForm


# Home view
class Home(View):  # class for inheriting 'home' view
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("core:profile_list")
        return render(request, "index.html")


# Profile view
@method_decorator(login_required, name="dispatch")
class ProfileList(View):
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()
        return render(request, "profileList.html", {"profiles": profiles})


# Create Profile view
class ProfileCreate(View):
    def get(self, request, *args, **kwargs):
        # form for creating profile
        form = ProfileForm()

        return render(request, "profileCreate.html", {"form": form})
