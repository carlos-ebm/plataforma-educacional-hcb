from django.contrib import admin
from .models import Activity, Activity_profile

# Register your models here.
class Activity_profileInLine(admin.TabularInline):
    model = Activity_profile
    extra = 1
    #readonly_field = ('created')

class ActivityAdmin(admin.ModelAdmin):
    inlines = [Activity_profileInLine,]

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Activity_profile)
