from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render
from django.views import View

from core.models import Url
from core.forms import UrlForm


class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = UrlForm(request.POST)
        if not form.is_valid():
            return render(request, self.template_name, {"form": form})

        url = form.cleaned_data.get("url")
        customhash = form.cleaned_data.get("hashed_url")
        input_pin = form.cleaned_data.get("input_pin")

        if customhash is None and input_pin is None:
            obj = Url.objects.create(url=url)
            short_url = obj.get_full_short_url(request)

            return render(
                request, self.template_name, {"short_url": short_url}
            )
        elif customhash:
            customhash = customhash[:10]
            try:
                obj = Url.objects.get(hashed_url=customhash)

                if input_pin is None or not obj.pin or input_pin != obj.pin:
                    form.add_error("input_pin", "The correct PIN is required to redefine this short url")
                    return render(request, self.template_name, {"form": form})

                obj.url = url
                obj.save()
            except ObjectDoesNotExist:
                obj = Url.objects.create(url=url, hashed_url=customhash)

            pin = obj.generate_pin()
            short_url = obj.get_full_short_url(request)

            return render(
                request, self.template_name, {"short_url": short_url, "pin": pin}
            )
        else:
            form.add_error(
                "hashed_url", "PINs are only needed with a custom hash"
            )
            return render(request, self.template_name, {"form": form})


class RedirectView(View):
    def get(self, request, hashed_url):
        try:
            url = Url.objects.get(hashed_url=hashed_url)
            return redirect(url.url)
        except Url.DoesNotExist:
            return redirect("home_page")
