from django.shortcuts import render
from django.views import View


class Home(View):  # class for inheriting 'home' view
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")
