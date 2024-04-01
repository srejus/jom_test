from django.shortcuts import render
from django.views import View

from .models import *

# Create your views here.
class IndexView(View):
    def get(self,request):
        todos = Todo.objects.filter(is_done=True)
        print(todos)
        return render(request,'index.html',{'tds':todos})
    
    def post(self,request):
        title = request.POST.get("title")
        desc = request.POST.get("desc")

        Todo.objects.create(title=title,desc=desc)
        return render(request,'contact.html')
