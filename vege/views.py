from django.shortcuts import render, redirect
from vege.models import reciepe

def receipes(request):
    if request.method == "POST":
        data = request.POST
        reciepe_name = data.get('reciepe_name')
        reciepe_desc = data.get('reciepe_desc')
        reciepe_image = request.FILES.get('reciepe_image')
        print(f'reciepe_name {reciepe_image}, reciepe_desc {reciepe_desc} reciepe_image {reciepe_image}')
    
        reciepe.objects.create(
            reciepe_name=reciepe_name,
            reciepe_desc=reciepe_desc,
            reciepe_image=reciepe_image
        )


        return redirect("/receipes/")

    queryset = reciepe.objects.all()
    context = {'vals': queryset}
    return render(request, "receipes.html", context)


def delete_receipes(request, id):
    queryset = reciepe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')


def update(request, id):
    queryset = reciepe.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        reciepe_name = data.get('reciepe_name')
        reciepe_desc = data.get('reciepe_desc')
        reciepe_image = request.FILES.get('reciepe_image')
        queryset.reciepe_name = reciepe_name
        queryset.reciepe_desc = reciepe_desc

        if reciepe_image:
            queryset.reciepe_image = reciepe_image
        queryset.save()
        return redirect('/receipes/')
    context  = {'update' : queryset}
    return render(request, "update.html", context)

