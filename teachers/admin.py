from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'birthday'
    ]

    list_per_page = 10

    search_fields = list_display

    list_filter = [
        'last_name'
    ]

    fields = [
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        'phone_number',
        'subject'
    ]

    def age(self, instance):
        return instance.get_age()

    readonly_fields = ['birthday', 'age']


admin.site.register(Teacher, TeacherAdmin)
