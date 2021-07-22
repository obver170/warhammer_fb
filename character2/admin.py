from django.contrib import admin
from .models import WeaponSkill, BallisticSkill, Strength, Toughness, Initiative, Agility, Dexterity, \
    Intelligence, Willpower, Fellowship

# Register your models here.


admin.site.register(WeaponSkill)
admin.site.register(BallisticSkill)
admin.site.register(Strength)
admin.site.register(Toughness)
admin.site.register(Initiative)
admin.site.register(Agility)
admin.site.register(Dexterity)
admin.site.register(Intelligence)
admin.site.register(Willpower)
admin.site.register(Fellowship)
