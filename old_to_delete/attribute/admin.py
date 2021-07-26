from django.contrib import admin
from .models import WeaponSkill, BallisticSkill, Strength, Toughness, Initiative, Agility, Dexterity, \
    Intelligence, Willpower, Fellowship, AttributeList, NameAttr


# Register your models here.
class AttrListAdmin(admin.ModelAdmin):
    list_display = ('name_list', 'weaponSkill', 'ballisticSkill', 'strength', 'toughness', 'initiative', 'agility', 'dexterity',
                    'intelligence', 'willpower', 'fellowship',)
    list_editable = ('weaponSkill', 'ballisticSkill', 'strength', 'toughness', 'initiative', 'agility', 'dexterity',
                    'intelligence', 'willpower', 'fellowship',)



admin.site.register(AttributeList, AttrListAdmin)
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
admin.site.register(NameAttr)
