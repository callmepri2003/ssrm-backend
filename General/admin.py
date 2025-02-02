from django.contrib import admin
import nested_admin

from General.models.Attendance import Attendance
from General.models.Group import Group
from General.models.Lesson import Lesson
from General.models.Reporting import Reporting
from General.models.Resource import Resource
from General.models.Enrolment import Enrolment
from General.models.Student import Student
from .models.Tutor import Tutor
from .models.Availability import Availability

# 1. Inline for Attendance inside Lesson
class AttendanceInline(nested_admin.NestedTabularInline):  # or NestedStackedInline
    model = Attendance
    extra = 0

# 2. Inline for Lesson inside Group
class LessonInline(nested_admin.NestedTabularInline):  # or NestedTabularInline
    model = Lesson
    extra = 0
    inlines = [AttendanceInline]  # ✅ Nest Attendance inside Lesson

# 3. Inline for Resource inside Group
class ResourceInline(nested_admin.NestedTabularInline):
    model = Resource
    extra = 1

class EnrolmentInline(nested_admin.NestedTabularInline):
    model = Enrolment
    extra = 1

# 5. Availability inline for Tutor
class AvailabilityInline(nested_admin.NestedTabularInline):
    model = Availability
    extra = 1

# 4. Group Admin (Contains Lesson & Resource)
@admin.register(Group)
class GroupAdmin(nested_admin.NestedModelAdmin):
    inlines = [ResourceInline, LessonInline, EnrolmentInline]  # ✅ Nest Lesson (which contains Attendance)

    list_display = ('__str__','estimatedProfit',)
    readonly_fields = ('estimatedProfit',)

    def estimatedProfit(self, obj):
        return f"${obj.estimatedProfit:.2f}"

    
    estimatedProfit.short_description = "Estimated Profit"

# 6. Tutor Admin
@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    inlines = [AvailabilityInline]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user','total_amount_spent_display',)
    readonly_fields = ('total_amount_spent_display',)
    inlines = [AttendanceInline]
    
    def total_amount_spent_display(self, obj):
        return f"${obj.total_amount_spent:.2f}"
    
    total_amount_spent_display.short_description = 'Total Spent'

@admin.register(Reporting)
class ReportingAdmin(admin.ModelAdmin):
    list_display = (
        'totalEstimatedWeeklyProfit', 
        'totalEnrolled',
        'averageLifetime'
        )
    readonly_fields = (
        'totalEstimatedWeeklyProfit', 
        'totalEnrolled',
        'averageLifetime'
        )

    def totalEstimatedWeeklyProfit(self, obj):
        return f"${obj.totalEstimatedWeeklyProfit:.2f}"
    
    def totalEnrolled(self, obj):
        return obj.totalEnrolled

    def averageLifetime(self, obj):
        return str(obj.averageLifetime)