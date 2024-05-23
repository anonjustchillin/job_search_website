from django.shortcuts import render, redirect
from job.models import Job, ApplyJob
from website.filter import JobFilter


def dashboard(request):
    if request.user.is_authenticated:
        filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
        context = {'filter': filter}
        return render(request, 'dashboard/dashboard.html', context)
    else:
        return redirect('home')
