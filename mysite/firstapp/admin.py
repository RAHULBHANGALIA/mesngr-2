from django.contrib import admin
import firstapp.models
admin.site.register(firstapp.models.Question)
admin.site.register(firstapp.models.Choice)

# Register your models here.
