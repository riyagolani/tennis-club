from django.contrib import admin

from members.models import Member

class MembersAdmin(admin.ModelAdmin):
    list_display = ('username', 'firstname')

admin.site.register(Member, MembersAdmin)

# Register your models here.
