from django.shortcuts import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from library.Connection import dbCursor

# Create your views here.

class MemberView(APIView):

    def get(self,request):
        # TODD: Argument로 페이징 처리하기, 정렬 처리
        sql = "SELECT" \
              " customerName," \
              " contactLastName," \
              " contactFirstName," \
              " phone" \
              " FROM customers" \
              " WHERE customerNumber < 200;"

        data = [
            dict(
                customerName=item['customerName'],
                contactLastName=item['contactLastName'],
                contactFirstName=item['contactFirstName'],
                phone=item['phone']
            ) for item in dbCursor(sql).get()
        ]

        return Response(data)