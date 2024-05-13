from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job
from .form import CreateJobForm, UpdateJobForm


# create a vacancy
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.company
                var.save()

                messages.info(request, 'Вакансія створена.')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Шось не то')
                return redirect('create-job')
        else:
            form = CreateJobForm()
            context = {'form': form}
            return render(request, 'job/create_job.html', context)
    else:
        messages.warning(request, 'Доступу немає')
        return redirect('dashboard')


# update a vacancy
def update_job(request, pk):
    job = Job.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateJobForm(request.POST, instance=job)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.company = request.company
            var.save()

            messages.info(request, 'Вакансія оновлена.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Шось не то')
    else:
        form = UpdateJobForm(instance=job)
        context = {'form': form}
        return render(request, 'job/update_job.html', context)


def manage_jobs(request):
    jobs = Job.objects.filter(user=request.user, company=request.user.company)
    context = {'jobs': jobs}
    return render(request, 'job/manage_jobs.html', context)
