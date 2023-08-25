from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse

cursor = connection.cursor()

def home(request):
    return render(request, 'home.html')


def test(request):
    try:
        cursor.execute('EXEC ddCMSNavigation')
        columns = [column[0] for column in cursor.description]
        print(columns)
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        print(result)
        print(type(result))
        return JsonResponse(result, safe=False)
    finally:
        cursor.close()