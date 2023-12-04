from django.shortcuts import render,redirect
from django.views.generic import View
from work.forms import EmpForm, BookForm, MoviesForm, FacultyForm, MobileForm, StudentNewForm
from work.models import Emp, Book, Movies, Faculty, Mobiles, StudentNew
# Create your views here.


class StudentNewView(View):
    def get(self,request):
        form = StudentNewForm()
        return render(request, "studentnew.html",{"form":form})
    
    def post(self,request):
        form = StudentNewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
           
            form = StudentNewForm()
            return render(request, "studentnew.html", {"form":form})
        else:
            return render(request, "studentnew.html",{"form":form}) 

class StudentList(View):
    def get(self,request):
        new = StudentNew.objects.all()
        return render(request, "studentnewlist.html",{"new":new})               


class MobilesView(View):
    def get(self, request):
        form = MobileForm()
        return render(request, "mobile.html",{"form":form})
    
    def post(self,request):
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            print("created all details of mobiles")
            form = MobileForm()
            return render(request, "mobile.html", {"form":form})
        
class MobileDetailView(View):
    def get(self,request):
        all =  Mobiles.objects.all()
        return render(request, "mobiledetail.html",{"all":all})
    
class MobileGetOne(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        one = Mobiles.objects.get(id=id)
        return render(request,"mobileone.html",{"one":one})
    
class MobileDelete(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        return redirect('mobile-all')   


class FacultyView(View):
    def get(self,request):
        form = FacultyForm()
        return render(request,"faculty.html",{"form":form})
    
    def post(self,request):
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            print("created")
            form = FacultyForm()
            return render(request, "faculty.html",{"form":form})
        else:
            return render(request,"faculty.html", {"form":form})
        
class FacultyList(View):
    def get(self,request):
        fac = Faculty.objects.all()
        return render(request, "facultylist.html",{"fac":fac})        
        
class MoviesView(View):
    def get(self,request):
        form = MoviesForm()
        return render(request, "movie.html", {"form":form})
    
    def post(self,request):
        form = MoviesForm(request.POST)
        if form.is_valid():
           form.save()
           # form.save(): method to add the data into database without using orm query(only for modelform)
           # modelname.objects.create(**form.cleaned_data) == ORM query
           print("created")
           form = MoviesForm()
           return render(request, "movie.html",{"form":form})
        else:
            return render(request, "movie.html",{"form":form})
        
class MovieList(View):
    def get(self,request):
        qs = Movies.objects.all()
        return render(request, "movielist.html", {"qs":qs}) 

class MovieDetailView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Movies.objects.get(id=id) 
        return render(request, "movieDetail.html",{"qs":qs})          

class BookView(View):
    def get(self,request):
        form = BookForm()
        return render(request, "book.html", {"form":form})
    
    def post(self,request):
        form = BookForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Book.objects.create(**form.cleaned_data)
            return render(request, "book.html", {"form":form})
        else:
            return render(request, "book.html", {"form":form})

class EmpView(View):

    def get(self,request):
        form = EmpForm()
        return render(request, "add.html",{"form":form})
    
    def post(self,request):
        form = EmpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Emp.objects.create(**form.cleaned_data)
            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})
       