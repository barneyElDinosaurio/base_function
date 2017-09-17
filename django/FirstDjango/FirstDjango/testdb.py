from django.http import HttpResponse
from TestModel.models import Test

def insert(request):
    test1=Test(name='Rocky')
    test1.save()
    return HttpResponse('Data insert successful')

def search(request):
    db_data=Test.objects.all()
    result=''
    for i in db_data:
        result=result+i.name+'\n'

    return HttpResponse(result)