from django.shortcuts import redirect, render
from app4_1.forms import Modelform1
from app4_1.models import Model1

# Create your views here.


def index(request):
    if request.method == "POST":

        personForm = Modelform1(request.POST)
        if personForm.is_valid():
            personForm.save()

    else:
        personForm = Modelform1()
    persons = Model1.objects.all()
    return render(
        request, "app4_1/index.html", {"forms": personForm, "persons": persons}
    )


def Update_view(request):
    if request.method == "POST":
        personForm = Modelform1(request.POST)
        if personForm.is_valid():
            personForm.save()
        return redirect("/app4_1/")

    else:
        id = request.GET.get("id")
        person = Model1.objects.get(id=id)
        personForm = Modelform1(instance=person)
        return render(
            request,
            "app4_1/update.html",
            {
                "forms": personForm,
            },
        )


def delete(request):
    id = request.GET.get("id")
    person = Model1.objects.get(id=id)
    person.delete()
    return redirect("/app4_1/")
