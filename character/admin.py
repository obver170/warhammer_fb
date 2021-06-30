from django.contrib import admin

from .models import Eyes, Nation, Hair, Sex, Metal, NumberMetal, Status

# Register your models here.

admin.site.register(Eyes)
admin.site.register(Nation)
admin.site.register(Hair)
admin.site.register(Sex)
admin.site.register(Metal)
admin.site.register(NumberMetal)
admin.site.register(Status)
