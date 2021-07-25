from django.contrib import admin
from .models import Character, Eyes, Party, Movement
from .health_models import Psychology, Mutation
# Register your models here.


admin.site.register(Character)
admin.site.register(Eyes)
admin.site.register(Party)
admin.site.register(Movement)
admin.site.register(Psychology)
admin.site.register(Mutation)

