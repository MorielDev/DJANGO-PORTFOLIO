from django.shortcuts import render, redirect, get_object_or_404
from .forms import PortfolioForm
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
    return render(request, 'hello/success.html', {'message': 'Portfolio created successfully!'})

def about_view(request):
    # Retrieve relevant data
    portfolio = Portfolio.objects.first()  # Retrieve the first portfolio object (adjust as needed)
    # Pass data to template
    return render(request, 'hello/about.html', {'portfolio': portfolio})

def resume(request):
    # Retrieve relevant data
    portfolios = Portfolio.objects.all()  # Retrieve all portfolio objects
    print("Number of portfolios:", len(portfolios))  # Debug statement to check the number of portfolios
    if portfolios:  # Check if portfolios exist
        print('yes print')  # Debug statement to indicate portfolios exist
    else:
        print('no print')  # Debug statement to indicate no portfolios
    # Pass data to template
    return render(request, 'hello/resume.html', {'portfolios': portfolios})

def fileout_view(request):
    # Retrieve relevant data
    portfolios = Portfolio.objects.all()  # Retrieve all portfolio objects
    print("Number of portfolios in fileout_view:", len(portfolios))  # Debug statement to check the number of portfolios
    if portfolios:  # Check if portfolios exist
        print('yes it collects')  # Debug statement to indicate portfolios exist
    else:
        print('no it does not')  # Debug statement to indicate no portfolios
    # Pass data to template
    return render(request, 'hello/fileout.html', {'portfolios': portfolios})
def my_view(request):
    portfolio = Portfolio.objects.get(pk=1)  # Assuming you have a Portfolio object
    return render(request, 'resume.html', {'portfolio': portfolio})