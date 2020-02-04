from django.contrib import admin
from account.models import Coordinator, Dean, Hod, Supervisor, StudentGroup


admin.site.register(Coordinator)
admin.site.register(Dean)
admin.site.register(Hod)
admin.site.register(Supervisor)
admin.site.register(StudentGroup)
