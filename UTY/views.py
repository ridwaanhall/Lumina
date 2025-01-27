from django.views import View
from django.http import HttpResponseRedirect

class RedirectView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('http://ridwaanhall.vercel.app/')