from django.shortcuts import render, redirect
from .models import Rating, Review
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def rateUser(request, receiverId):
    if request.method == 'POST':
        score = request.POST.get('score')
        rating = Rating.objects.create(
            author=request.user,
            receiverId = receiverId,
            score=score
        )
        # da cambiare con la pagina del profilo //TODO
        return redirect('pagina_profilo', receiverId)
    else:
        # attenzione alla pagina html //TODO
        return render(request, 'rating.html', {'receiverId': receiverId})

@login_required
def reviewUser(request, receiverId):
    if request.method == 'POST':
        text = request.POST.get('testo')
        review = Review.objects.create(
            author=request.user,
            receiverId=receiverId,
            text=text
        )
        # da cambiare con la pagina del profilo //TODO
        return redirect('pagina_profilo', receiverId)
    else:
        # attenzione alla pagina html //TODO
        return render(request, 'review.html', {'receiverId': receiverId})