from django.contrib import admin
from .models import SkillOther, SkillPro, ListOtherSkills, BaseSkillOther, BaseSkillPro, BaseTalent, Talent
# Register your models here.

admin.site.register(SkillOther)
admin.site.register(SkillPro)
admin.site.register(ListOtherSkills)
admin.site.register(BaseSkillOther)
admin.site.register(BaseSkillPro)
admin.site.register(BaseTalent)
admin.site.register(Talent)