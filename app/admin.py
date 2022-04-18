from django.contrib import admin

from app.models import AccessRecords, Topic, webpage

# Register your models here.


admin.site.register(Topic)


admin.site.register(webpage)

admin.site.register(AccessRecords)

