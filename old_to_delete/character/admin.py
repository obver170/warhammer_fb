from django.contrib import admin

from .models import Eyes, Nation, Hair, Sex, Metal, NumberMetal, Status, Talent, CurrentTalent, Character, Class,\
    Career, Species, Attribute, SetAttributes, Skill, NameAttribute, NameSkill

# Register your models here.

admin.site.register(Eyes)
admin.site.register(Nation)
admin.site.register(Hair)
admin.site.register(Sex)
admin.site.register(Metal)
admin.site.register(NumberMetal)
admin.site.register(Status)
admin.site.register(Talent)
admin.site.register(CurrentTalent)
admin.site.register(Character)
admin.site.register(Class)
admin.site.register(Career)
admin.site.register(Species)
admin.site.register(NameAttribute)
admin.site.register(Attribute)
admin.site.register(SetAttributes)
admin.site.register(NameSkill)
admin.site.register(Skill)
