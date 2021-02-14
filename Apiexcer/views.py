import json

from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from library.Connection import dbCursor


# Create your views here.

class MemberView(APIView):

    def get(self,request):
        sql = "SELECT * FROM customers WHERE customerNumber < 200;"
        read = dbCursor(sql)

        return HttpResponse(json.dumps(read.get()))
