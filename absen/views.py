from django.shortcuts import render
from django.views import View

from . import about_data

class LuminaAppView(View):
    def get(self, request):
        try:
            return render(request, 'absen/absen.html')
        except (FileNotFoundError, ImportError) as e:
            context = {
                'error_code': 500,
                'error_message': f'Module Error: {e}'
            }
            return render(request, 'error.html', context, status=500)
        except Exception as e:
            context = {
                'error_code': 500,
                'error_message': f'Unexpected Error: {e}'
            }
            return render(request, 'error.html', context, status=500)
        
class LuminaSecAppView(View):
    def get(self, request):
        try:
            return render(request, 'absen/absen_sec.html')
        except (FileNotFoundError, ImportError) as e:
            context = {
                'error_code': 500,
                'error_message': f'Module Error: {e}'
            }
            return render(request, 'error.html', context, status=500)
        except Exception as e:
            context = {
                'error_code': 500,
                'error_message': f'Unexpected Error: {e}'
            }
            return render(request, 'error.html', context, status=500)
        
class LuminaSimpleAppView(View):
    def get(self, request):
        try:
            return render(request, 'absen/simple.html')
        except (FileNotFoundError, ImportError) as e:
            context = {
                'error_code': 500,
                'error_message': f'Module Error: {e}'
            }
            return render(request, 'error.html', context, status=500)
        except Exception as e:
            context = {
                'error_code': 500,
                'error_message': f'Unexpected Error: {e}'
            }
            return render(request, 'error.html', context, status=500)

class TermsView(View):
    def get(self, request):
        try:
            return render(request, 'absen/terms.html')
        except (FileNotFoundError, ImportError) as e:
            context = {
                'error_code': 500,
                'error_message': f'Module Error: {e}'
            }
            return render(request, 'error.html', context, status=500)
        except Exception as e:
            context = {
                'error_code': 500,
                'error_message': f'Unexpected Error: {e}'
            }
            return render(request, 'error.html', context, status=500)

class AboutView(View):
    def get(self, request):
        try:
            about_sections = about_data.AboutData.about

            context = {
                'about_sections': about_sections,
            }

            return render(request, 'absen/about.html', context)
        except (FileNotFoundError, ImportError) as e:
            context = {
                'error_code': 500,
                'error_message': f'Module Error: {e}'
            }
            return render(request, 'error.html', context, status=500)
        except Exception as e:
            context = {
                'error_code': 500,
                'error_message': f'Unexpected Error: {e}'
            }
            return render(request, 'error.html', context, status=500)