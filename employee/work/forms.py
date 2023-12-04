from django import forms
from work.models import Movies, Faculty, Mobiles, StudentNew


class EmpForm(forms.Form):
    name = forms.CharField()
    place = forms.CharField()
    salary = forms.CharField()
    contact = forms.CharField()

class BookForm(forms.Form):
    title = forms.CharField()  
    author = forms.CharField() 
    publication_year = forms.CharField() 
    genre = forms.CharField()

class MoviesForm(forms.ModelForm):

    class Meta:
        model = Movies
        fields = '__all__'    

class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty
        fields = '__all__'     

class MobileForm(forms.ModelForm):

    class Meta:
        model = Mobiles
        fields ='__all__'

class StudentNewForm(forms.ModelForm):

    class Meta:
        model = StudentNew
        fields = '__all__'        