from django.contrib import admin
from .models import ProfessionalSkillList, OtherSkillList, Gamble, OutdoorSurvival, TrainingOfAnimals, Knowledge, \
    BookSearches, Treatment, Veterinarian, Grade, SecretSigns, Language



# Register your models here.

admin.site.register(ProfessionalSkillList)
admin.site.register(TrainingOfAnimals)
admin.site.register(Knowledge)
admin.site.register(BookSearches)
admin.site.register(Treatment)
admin.site.register(Veterinarian)
admin.site.register(Grade)
admin.site.register(SecretSigns)
admin.site.register(Language)






admin.site.register(OtherSkillList)
admin.site.register(Gamble)
admin.site.register(OutdoorSurvival)
