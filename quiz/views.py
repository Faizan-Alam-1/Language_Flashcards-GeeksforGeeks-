from django.shortcuts import render
from apps.models import Addcard

def quiz(request):
    obj = Addcard.objects.order_by("?")
    score = 0 
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        if Addcard.objects.filter(input_box=input_data).exists():
            score +=1


    return render(request, "quiz/quiz.html", {"obj":obj , "score" : score})
