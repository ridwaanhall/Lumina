from django.shortcuts import render
from django.views import View

# Create your views here.
class LuminaAppView(View):
    def get(self, request):
        return render(request, 'absen/absen.html')
    
class TermsView(View):
    def get(self, request):
        return render(request, 'absen/terms.html')