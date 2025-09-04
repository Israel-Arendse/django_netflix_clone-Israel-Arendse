from django.shortcuts import redirect, render
from django.views import View

# Import login_requred and method_decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Import from core/forms.py
from .forms import ProfileForm
from core.models import Profile


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
        # Form for creating profile
        form = ProfileForm()
        return render(request, "profileCreate.html", {"form": form})

    # Post method
    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST or None)

        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect("core:profile_list")
        else:
            print(form.errors)

        return render(request, "profileCreate.html", {"form": form})
