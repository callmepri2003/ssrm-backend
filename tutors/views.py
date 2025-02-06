from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render

from General.models.Attendance import Attendance
from General.models.Group import Group
from General.models.Lesson import Lesson
from General.models.Student import Student
from General.models.Tutor import Tutor

from django.contrib import messages


def is_tutor(user):
    return user.groups.filter(name="tutors").exists()

@login_required
@user_passes_test(is_tutor)
def dashboard_view(request):
    tutor = Tutor.objects.get(user = request.user)
    groups = list(tutor.groups.all())
    context = {
        'groups': groups
    }
    return render(request, 'tutors/dashboard.html', context)

@login_required
@user_passes_test(is_tutor)
def create_lesson(request):
    if request.method == 'POST':
        try:
            group = Group.objects.get(id=request.POST.get('group_id'))
            date_time = request.POST.get('date_time')
            comments = request.POST.get('comments', '')
            student_ids = request.POST.getlist('student_ids')

            # Create lesson
            lesson = Lesson.objects.create(
                group=group,
                tutor=request.user.tutor.all()[0],
                dateTime=date_time,
                comments=comments,
                status='completed'
            )

            # Create attendance records
            for student_id in student_ids:
                student = Student.objects.get(id=student_id)
                Attendance.objects.create(
                    student=student,
                    lesson=lesson,
                    trial=False  # Modify if needed
                )

            messages.success(request, 'Lesson created successfully!')
        except Exception as e:
            messages.error(request, f'Error creating lesson: {str(e)}')

        return redirect('/')
    print("skipped")
    return redirect('/')


def calendar_view(request):
    return render(request, 'tutors/calendar.html', {})