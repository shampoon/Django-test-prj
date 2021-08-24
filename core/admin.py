from django.contrib import admin
import core.models

admin.site.register(core.models.Human)
admin.site.register(core.models.Industry)
admin.site.register(core.models.Company)

