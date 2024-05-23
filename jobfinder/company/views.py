from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Company
from .form import CompanyForm
from users.models import User


# update company
def update_company(request):
    if request.user.is_authenticated and request.user.is_recruiter:
        company = Company.objects.get(user=request.user)
        if request.method == 'POST':
            form = CompanyForm(request.POST, instance=company)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(pk=request.user.id)
                user.has_resume = True
                user.save()
                var.save()

                messages.info(request, 'Компанія оновлена')
                return redirect('dashboard')

            else:
                messages.warning(request, 'Неправильно введені дані')

        else:
            form = CompanyForm(instance=company)
            context = {'form': form}
            return render(request, 'company/company.html', context)
    else:
        messages.warning(request, 'Доступу немає')
        return redirect('dashboard')


# view company details
def company_details(request, pk):
    if request.user.is_authenticated and request.user.is_recruiter:
        company = Company.objects.get(pk=pk)
        context = {'company': company}
        return render(request, 'company/company_details.html', context)
    else:
        return redirect('home')
