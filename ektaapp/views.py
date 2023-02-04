from django.shortcuts import render
from django.views import View
from linkedin_api import Linkedin
from reportlab.pdfgen import canvas  
from django.http import HttpResponse
# Create your views here.

context = {}
def download_pdf(request):
    print("context----",context)
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 20)  
    p.drawString(100,100, "Ekta Solve more crimes.")
    p.drawString(100,100, f"Full Name: {context['profile']['firstName']} {context['profile']['lastName']}")
    p.save()  
    return response

class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

class HomeView(View):
    def get(self, request):
        # Authenticate using any Linkedin account credentials
        return render(request, "index.html")
    
    def post(self, request):
        global context
        api = Linkedin('yashgarg11131@gmail.com', 'Opentheaccount@123')
        if "linkedin" in request.POST:
            profile = api.get_profile(request.POST["linkedin"])
            contact_info = api.get_profile_contact_info(request.POST["linkedin"])
            context = {**context, **contact_info, **contact_info["phone_numbers"][0], **{"profile": profile}}
        return render(request, "index.html", context)


