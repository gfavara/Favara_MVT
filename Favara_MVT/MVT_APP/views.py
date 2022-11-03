from django.shortcuts import render
from .models import Familiar

# Create your views here.
def familia(request):

    fam1=Familiar(nombre="Juan Carlos",apellido="Favara",parentezco="Padre",dni=1,fecha_nac="06/02/1960")
    fam2=Familiar(nombre="Rosana",apellido="Dell Aquila",parentezco="Madre",dni=2,fecha_nac="28/05/1958")
    fam3=Familiar(nombre="Gladiz",apellido="Gabrielli",parentezco="Abuela",dni=3,fecha_nac="08/01/1933")

    return render(request, 'familia.html',{'familia':[fam1,fam2,fam3]})


     
    