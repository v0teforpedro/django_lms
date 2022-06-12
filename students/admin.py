from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = [
        'first_name',
        'last_name',
        'group'
    ]

    list_display_links = list_display

    list_per_page = 10

    search_fields = [
        'first_name',
        'last_name'
    ]

    list_filter = [
        'group'
    ]

    fields = [
        ('first_name', 'last_name'),
        ('birthday', 'age'),
        'phone_number',
        'group',
    ]

    def age(self, instance):
        return instance.get_age()

    age.short_description = 'Age of student'

    readonly_fields = ['birthday', 'age']


admin.site.register(Student, StudentAdmin)
