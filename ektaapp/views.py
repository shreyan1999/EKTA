from django.shortcuts import render
from django.views import View
from linkedin_api import Linkedin
from reportlab.pdfgen import canvas  
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

context = {}
class DownloadPDF(APIView):
    def get(self, request):
        print(context)
        response = HttpResponse(content_type='application/pdf')  
        response['Content-Disposition'] = f"""attachment; filename="ys123.pdf"""  
        p = canvas.Canvas(response)  
        p.setFont("Times-Roman", 20)  
        p.drawString(100,100, "Ekta Solve more crimes.")
        p.drawString(100,100, f"Full Name: ")
        p.save()
        return response

class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

class HomeView(View):
    def get(self, request):
        # Authenticate using any Linkedin account credentials
        return render(request, "index.html")
    # def post(self, request):
    #     global username
    #     if "linkedin" in request.POST:
    #         username = request.POST["linkedin"]
    #     return render(request, "index.html", context)
    
    
    
class LinkedInDATAAPI(APIView):
    def post(self, request):
        global context
        api = Linkedin('yashgarg11131@gmail.com', 'Opentheaccount@123')
        data = request.data
        try:
            profile = api.get_profile(data["linkedin"])
            contact_info = api.get_profile_contact_info(data["linkedin"])
        except:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": "Result not found."}, status=status.HTTP_404_NOT_FOUND)
        context = {"status": status.HTTP_200_OK, "message": "Data found successfully.", "profile": profile, "contact_info": contact_info}
        return Response({"status": status.HTTP_200_OK, "message": "Data found successfully.", "profile": profile, "contact_info": contact_info}, status=status.HTTP_200_OK)