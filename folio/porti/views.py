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
    # Check if the request is coming from the 'about' URL
    if request.path == '/about/':
        # Retrieve data only if accessed from the 'about' URL
        portfolio = Portfolio.objects.first()  # Adjust this to retrieve the appropriate portfolio
        return render(request, 'hello/about.html', {'portfolio': portfolio})
    else:
        # If accessed from a different URL, render without data
        return render(request, 'hello/about.html')


def resume(request):
    return render(request, 'hello/resume.html')  # Render the resume page

def fileout_view(request):
    # Your logic here, for example, passing context to a template
    context = {'data': 'some data'}
    return render(request, 'hello/fileout.html', context)

def about_view(request):
    # Retrieve relevant data
    # For example:
    portfolio = Portfolio.objects.first()  # Retrieve the first portfolio object (adjust as needed)
    # Pass data to template
    return render(request, 'hello/about.html', {'portfolio': portfolio})

def resume(request):
    # Retrieve relevant data
    # For example:
    portfolios = Portfolio.objects.all()  # Retrieve all portfolio objects
    # Pass data to template
    return render(request, 'hello/resume.html', {'portfolios': portfolios})

def fileout_view(request):
    # Retrieve relevant data
    # For example:
    portfolios = Portfolio.objects.all()  # Retrieve all portfolio objects
    # Pass data to template
    return render(request, 'hello/fileout.html', {'portfolios': portfolios})

