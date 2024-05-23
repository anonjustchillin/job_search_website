from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume
from users.models import User
from .form import ResumeForm


# оновити резюме
def update_resume(request):
    if request.user.is_authenticated and request.user.is_applicant:
        resume = Resume.objects.get(user=request.user)
        if request.method == 'POST':
            form = ResumeForm(request.POST, request.FILES, instance=resume)
            if form.is_valid():
                var = form.save(commit=False)
                user = User.objects.get(pk=request.user.id)
                user.has_resume = True
                user.save()
                var.save()

                messages.info(request, 'Резюме оновлене')
                return redirect('dashboard')

            else:
                messages.warning(request, 'Неправильно введені дані')
        else:
            form = ResumeForm(instance=resume)
            context = {'form': form}
            return render(request, 'resume/resume.html', context)
    else:
        messages.warning(request, 'Доступу немає')
        return redirect('dashboard')


# перегляд резюме
def resume_details(request, pk):
    if request.user.is_authenticated and request.user.is_applicant:
        resume = Resume.objects.get(pk=pk)
        context = {'resume': resume}
        return render(request, 'resume/resume_details.html', context)
    else:
        return redirect('home')


# def download(request, pk):
#     return FileResponse(open(path_to_file, 'rb'), as_attachment=True)
