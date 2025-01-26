from django.shortcuts import render
from django.views import View

# Create your views here.
class AbsenView(View):
    def get(self, request):
        return render(request, 'absen/absen.html')