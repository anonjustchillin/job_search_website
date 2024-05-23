from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Job, ApplyJob
from .form import CreateJobForm, UpdateJobForm


# create a vacancy
def create_job(request):
    if request.user.is_recruiter and request.user.has_company:
        if request.method == 'POST':
            form = CreateJobForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()

                messages.info(request, 'Вакансія створена')
                return redirect('dashboard')
            else:
                messages.warning(request, 'Сталася помилка')
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
    if request.user.is_authenticated and request.user.is_recruiter:
        job = Job.objects.get(pk=pk)
        if request.method == 'POST':
            form = UpdateJobForm(request.POST, instance=job)
            if form.is_valid():
                var = form.save(commit=False)
                var.user = request.user
                var.company = request.user.company
                var.save()

                messages.info(request, 'Вакансія оновлена')
                return redirect('job/manage_jobs.html')
            else:
                messages.warning(request, 'Сталася помилка')
        else:
            form = UpdateJobForm(instance=job)
            context = {'form': form}
            return render(request, 'job/update_job.html', context)
    else:
        return redirect('home')


def manage_jobs(request):
    if request.user.is_authenticated and request.user.is_recruiter:
        jobs = Job.objects.filter(user=request.user, company=request.user.company)
        context = {'jobs': jobs}
        return render(request, 'job/manage_jobs.html', context)
    else:
        return redirect('home')


def delete_job(request, pk):
    if request.user.is_authenticated and request.user.is_recruiter:
        job = Job.objects.get(pk=pk)
        job.delete()
        messages.info(request, 'Вакансія видалена')
        return redirect('manage-jobs')
    else:
        return redirect('home')


def apply_to_job(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        job = Job.objects.get(pk=pk)
        if ApplyJob.objects.filter(user=request.user, job=pk).exists():
            messages.warning(request, 'Доступу немає')
            return redirect('dashboard')
        else:
            ApplyJob.objects.create(
                job=job,
                user=request.user
            )
            messages.info(request, 'Ви відправили заявку на вакансію')
            return redirect('dashboard')
    else:
        messages.info(request, 'Увійдіть у свій акаунт')
        return redirect('login')


def all_applicants(request, pk):
    if request.user.is_authenticated and request.user.is_recruiter:
        job = Job.objects.get(pk=pk)
        applicants = job.applyjob_set.all()
        context = {'job': job, 'applicants': applicants}
        return render(request, 'job/all_applicants.html', context)
    else:
        return redirect('home')


def applied_jobs(request):
    if request.user.is_authenticated and request.user.is_applicant:
        jobs = ApplyJob.objects.filter(user=request.user)
        context = {'jobs': jobs}
        return render(request, 'job/applied_job.html', context)
    else:
        return redirect('home')
