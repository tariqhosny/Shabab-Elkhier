from django.shortcuts import render

# Create your views here.
def importData(request):
    return render(request, 'importData/importData.html')
