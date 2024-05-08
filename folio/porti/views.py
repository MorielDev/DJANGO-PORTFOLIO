from django.shortcuts import render, redirect
from .forms import PortfolioForm
from django.shortcuts import render, get_object_or_404
from .models import Portfolio
# Create your views here.

def create_portfolio(request):
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            new_portfolio = form.save()
            return redirect('portfolio_detail', id=new_portfolio.id)  # Redirects immediately to the detail page
    else:
        form = PortfolioForm()
    return render(request, 'hello/index.html', {'form': form})


def list_portfolios(request):
    portfolios = Portfolio.objects.all()
    return render(request, 'hello/fileout.html', {'portfolios': portfolios})


def portfolio_detail(request, id):
    portfolio = get_object_or_404(Portfolio, pk=id)
    print("Portfolio fetched:", portfolio)
    return render(request, 'hello/fileout.html', {'portfolio': portfolio})


def success_page(request):
    print("Redirected to success page.")
    return render(request, 'hello/fileout.html', {'message': 'Portfolio created successfully!'})




