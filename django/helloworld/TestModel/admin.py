from django.contrib import admin
from TestModel.models import Test, Contact, Tag

# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     fields = ("name", "email")


# class ContactAdmin(admin.ModelAdmin):
#    fieldsets = (
#        ['Main',{
#            "fields": ("name", "email")
#        }],
#        ["Advance", {
#            'classes': ('collapse',),  # CSS
#            'fields': ('age',),
#        }]
#    )

# 内联（inline）显示
class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "age", "email")  # list
    search_fields = ("name",)
    inlines = [TagInline]  # Inline
    fieldsets = (
       ['Main', {
           "fields": ("name", "email")
       }],
       ["Advance", {
           'classes': ('collapse',),  # CSS
           'fields': ('age',),
       }]
   )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])