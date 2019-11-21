from django.shortcuts import render

# Create your views here.

from .serializers import *
from django.http import HttpResponse,JsonResponse
from django.shortcuts import redirect
from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated







def index(request):
    try:
        if request.method=="GET":
            if request.user.is_authenticated():
                return HttpResponseRedirect('/dashboard/')
            return render(request,'index.html')
        else:
            username = request.POST.get('uname', '')
            password = request.POST.get('psw', '')
            user = auth.authenticate(username = username, password = password)       
            if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect('/dashboard/')
            else:
                return render(request,'index.html')
    except Exception as er:
        return HttpResponse('Getting the following error ',er)



@login_required
def user_logout(request):
    try:
        auth.logout(request)
        return HttpResponseRedirect('/')
    except Exception as er:
        return HttpResponse('Getting the following error ',er)




def dashboard(request):
    try:
        if request.user.is_authenticated():
            return render(request,'dashboard.html')
        return HttpResponseRedirect('/')
    except Exception as er:
        # return render(request,'dashboard.html')
        return HttpResponse('Getting the following errorrrrrrr ')







# class BookData(APIView):
#     authentication_classes = (SessionAuthentication,BasicAuthentication)
#     permission_classes = (IsAuthenticated,)
#     def get(self,request):
#         try:
#             # import ipdb;ipdb.set_trace()
#             book_id = request.GET.get('book_id')
#             if book_id:
#                 book_obj = BookDetails.objects.filter(pk=book_id)
#                 obj = BookSerializer(book_obj,many=True)
#                 # return Response(obj.data)
#             else:
#                 book_obj = BookDetails.objects.all()
#                 obj = BookSerializer(book_obj,many=True)
#             return Response(obj.data)
#         except Exception as er:
#             return Response('Getting the following error while retriving the data')






class BookData(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def get(self,request):
        try:
            book_id =request.GET.get('book_id')
            if book_id:
                book_obj = BookDetails.objects.filter(pk=book_id)
            else:
                book_obj = BookDetails.objects.all()
            obj = BookSerializer(book_obj,many=True)
            return Response(obj.data)
        except Exception as er:
            return Response("Failed")

    def post(self,request):
        try:
            # import ipdb;ipdb.set_trace()
            book_name = request.data[0].get('book_name')
            b_nob = request.data[0].get('nob')
            b_rack = request.data[0].get('rack')
            user_obj = User.objects.get(pk=request.user.id)
            BookDetails.objects.create(book_name=book_name,
                                        num_of_books=b_nob,
                                        rack_number=b_rack,
                                        author_id=user_obj)
            return Response('Saved Successfully')
        except Exception as er:
            return Response("Failed")
    def put(self,request):
        try:
            book_id = request.data[0].get('book_id')
            book_name = request.data[0].get('book_name')
            b_nob = request.data[0].get('nob')
            b_rack = request.data[0].get('rack')
            user_obj = User.objects.get(pk=request.user.id)
            update_book = BookDetails.objects.filter(pk = book_id)
            update_book.update(book_name=book_name,
                                num_of_books=b_nob,
                                rack_number=b_rack)
            return Response('Updated Successfully')
        except Exception as er:
            return Response("Failed")
    def delete(self,request):
        try:
            book_id =request.GET.get('book_id')
            BookDetails.objects.filter(pk=book_id).delete()
            return Response('Deleted Successfully')
        except Exception as er:
            return Response("Failed")



