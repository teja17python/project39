from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Product
# Create your views here.
class ProductInput(View):
    def get(self,request):
        return render(request,'productinput.html')
class ProductInsert(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p_name=request.GET["t2"]
        p_cost=float(request.GET["t3"])
        p_mfdt=request.GET["t4"]
        p_expdt=request.GET["t5"]
        p1=Product(pid=p_id,pname=p_name,pcost=p_cost,pmfdt=p_mfdt,pexpdt=p_expdt)
        p1.save()
        return HttpResponse("product inserted successfully")
class ProductDisplay(View):
    def get(self,request):
        recs=Product.objects.all()
        mydict={'records':recs}
        return render(request,'display.html',context=mydict)
class ProductDeleteInput(View):
    def get(self,request):
        return render(request,'deleteinput.html')
class ProductDelete(View):
    def get(self,request):
        p_id=int(request.GET["t1"])
        p1=Product.objects.filter(pid=p_id)
        if p1:
            p1.delete()
            return HttpResponse("product deleted successfully")
        else:
            return HttpResponse("product does not exists")
class ProductUpdateInput(View):
    def get(self,request):
        return render(request,'updateinput.html')
class ProductUpdate(View):
    def get(self,request):
        p_id = int(request.GET["t1"])
        p_name = request.GET["t2"]
        p_cost = float(request.GET["t3"])
        p_mfdt = request.GET["t4"]
        p_expdt = request.GET["t5"]
        p=Product.objects.get(pid=p_id)
        p.pname=p_name
        p.pcost=p_cost
        p.pmfdt=p_mfdt
        p.pexpdt=p_expdt
        p.save()
        return HttpResponse("product updated successfully")