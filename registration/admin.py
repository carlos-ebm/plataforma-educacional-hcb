from django.contrib import admin
from .models import Profile, Profile_activity

# Register your models here.
class Profile_activityInLine(admin.TabularInline):
    model = Profile_activity
    extra = 1
    readonly_field = ('created')

class ProfileAdmin(admin.ModelAdmin):
    inlines = [Profile_activityInLine,]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Profile_activity)