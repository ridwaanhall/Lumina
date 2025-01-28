from django.views import View
from django.http import HttpResponseRedirect

class PortfolioWebsiteView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('https://ridwaanhall.vercel.app/')

class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect('https://ngoding-me.vercel.app/')