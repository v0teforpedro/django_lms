from django.contrib import admin

from students.models import Student

from .models import Group


class StudentsInlineTable(admin.TabularInline):
    model = Student
    fields = [
        'first_name',
        'last_name',
        'birthday',
        'phone_number'
    ]

    # amount of empty fields in table
    extra = 0

    readonly_fields = fields

    show_change_link = True

    # turn off table add
    def has_add_permission(self, request, obj):
        return False

    # turn off table delete
    def has_delete_permission(self, request, obj=None):
        return False


class TeachersInlineTable(admin.TabularInline):
    model = Group.teachers.through
    fields = [
        'first_name',
        'last_name',
        'subject'
    ]

    extra = 0

    def first_name(self, obj):
        return obj.teacher.first_name

    def last_name(self, obj):
        return obj.teacher.last_name

    def subject(self, obj):
        return obj.teacher.subject

    readonly_fields = fields

    show_change_link = True

    def has_add_permission(self, request, obj):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class GroupAdmin(admin.ModelAdmin):
    list_display = [
        'group_name',
        'max_capacity',
        'headman'
    ]

    fields = [
        'group_name',
        ('curr_capacity', 'max_capacity'),
        'headman',
        'teachers',
    ]

    def curr_capacity(self, instance):
        return instance.student_count

    curr_capacity.short_description = 'Current students amount'

    readonly_fields = ['curr_capacity', 'max_capacity']

    inlines = [StudentsInlineTable, TeachersInlineTable]

    # disables option to add headman via actions
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        return form


admin.site.register(Group, GroupAdmin)
