from django.contrib import admin
from .models import Character, Eyes, Party, Movement
from .modellist.health_models import Psychology, Mutation
from .modellist.career_models import Class, Career, Nation, Estate, ListArchiveCarriers
from .modellist.skill_models import SkillOther, SkillPro, ListOtherSkills, BaseSkillOther, BaseSkillPro, BaseTalent, \
    Talent
from .modellist.attr_models import WeaponSkill, BallisticSkill, Strength, Toughness, Initiative, Agility, Dexterity, \
    Intelligence, Willpower, Fellowship, AttributeList, NameAttr

# Register your models here.


admin.site.register(Character)
admin.site.register(Eyes)
admin.site.register(Party)
admin.site.register(Movement)
admin.site.register(Psychology)
admin.site.register(Mutation)

# Карьера
admin.site.register(Class)
admin.site.register(Career)
admin.site.register(Nation)
admin.site.register(Estate)
admin.site.register(ListArchiveCarriers)

# Навыки
admin.site.register(SkillOther)
admin.site.register(SkillPro)
admin.site.register(ListOtherSkills)
admin.site.register(BaseSkillOther)
admin.site.register(BaseSkillPro)
admin.site.register(BaseTalent)
admin.site.register(Talent)


# Характеристики
class AttrListAdmin(admin.ModelAdmin):
    list_display = (
    'name_list', 'weaponSkill', 'ballisticSkill', 'strength', 'toughness', 'initiative', 'agility', 'dexterity',
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
