from django.shortcuts import render, redirect
from .forms import PortfolioForm
from django.shortcuts import render, get_object_or_404
from .models import Portfolio
# Create your views here.

def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect as appropriate
    else:
        form = PortfolioForm()
    return render(request, 'hello/index.html', {'form': form})



def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, pk=id)
    return render(request, 'hello/fileout.html', {'portfolio': portfolio})
