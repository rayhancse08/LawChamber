from django.contrib import admin
from .models import Bank,Branch,File,Doc
from home.models import *

class AboutUsAdmin(admin.ModelAdmin):
    list_display=['titles','body']
    class Meta:
        model=AboutUs

class ContactAdmin(admin.ModelAdmin):
    list_display=['address','phoneNumber','email']
    class Meta:
        model=Contact


class BankAdmin(admin.ModelAdmin):
    list_display=['name']

class BranchAdmin(admin.ModelAdmin):
    list_display=['bank','name','address']

class DocInline(admin.StackedInline):
    list_display=['name','doc']
    model=Doc

class FileAdmin(admin.ModelAdmin):
    list_display = ['name', 'bill', 'bank','branch','account_no']
    inlines = [
        DocInline
    ]
    class Meta:
        model=File

admin.site.register(Bank,BankAdmin)
admin.site.register(Branch,BranchAdmin)
admin.site.register(File,FileAdmin)
# Register your models here.
admin.site.register(AboutUs,AboutUsAdmin)
admin.site.register(Contact,ContactAdmin)