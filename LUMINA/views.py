from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.core.exceptions import SuspiciousOperation
from urllib.parse import urlparse

class PortfolioWebsiteView(View):
    def get(self, request, *args, **kwargs):
        try:
            url = 'https://ridwaanhall.vercel.app/'
            if not urlparse(url).scheme or not urlparse(url).netloc:
                raise SuspiciousOperation("Invalid redirect URL")
            return HttpResponseRedirect(url)
        except SuspiciousOperation as e:
            context = {
                'error_code': 400,
                'error_message': f'Bad Request: {e}'
            }
            return render(request, 'error.html', context, status=400)
        except Exception as e:
            context = {
                'error_code': 500,
                'error_message': f'Internal Server Error: {e}'
            }
            return render(request, 'error.html', context, status=500)

class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        try:
            url = 'https://ngoding-me.vercel.app/'
            if not urlparse(url).scheme or not urlparse(url).netloc:
                raise SuspiciousOperation("Invalid redirect URL")
            return HttpResponseRedirect(url)
        except SuspiciousOperation as e:
            context = {
                'error_code': 400,
                'error_message': f'Bad Request: {e}'
            }
            return render(request, 'error.html', context, status=400)
        except Exception as e:
            context = {
                'error_code': 500,
                'error_message': f'Internal Server Error: {e}'
            }
            return render(request, 'error.html', context, status=500)

class CatchAllView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'error_code': 404
        }
        return render(request, 'error.html', context, status=404)