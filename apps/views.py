from django.shortcuts import render ,redirect ,get_object_or_404
from .models import Addcard
from .forms import Addcardform

def Home(request):
    data = Addcard.objects.all()
    return render(request , 'Home.html' , {'data':data})

def Addcards(request):
    if request.method == 'POST':
        form = Addcardform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Home')        
    else:
        form = Addcardform()      

    return render(request,'Addcard.html' , {'form': form})


def Deletecard(request , id):
    data_instance = Addcard.objects.get(id=id)
    data_instance.delete()
    return redirect('Home')


def Updatecard(request , id):
    instance = get_object_or_404(Addcard, id=id)
    if request.method == 'POST':
        form = Addcardform(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('Home') 
    else:
        form = Addcardform(instance=instance)

    return render(request, 'Update.html', {'form': form})    
    

