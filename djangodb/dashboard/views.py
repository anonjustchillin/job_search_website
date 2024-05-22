from django.shortcuts import render
from job.models import Job, ApplyJob
from website.filter import JobFilter


def dashboard(request):
    filter = JobFilter(request.GET, queryset=Job.objects.filter(is_available=True).order_by('-timestamp'))
    context = {'filter': filter}
    return render(request, 'dashboard/dashboard.html', context)
