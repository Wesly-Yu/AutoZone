from django.contrib import admin
from apptest.models  import Appcase,Appcasestep
from datetime import datetime

# Register your models here.
class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcase_models','appcasename','appcasedesc','appteststep','appcase_charger','creat_time']
    model = Appcase
    extra = 1

class AppcasestepAdmin(admin.TabularInline):
    list_display = ['apptestlocation','appfindmethod','appkwargesone','appkwargestwo','appkwargesthree','appassertdata','apptestresult','appcomments','Appcase','id']
    model = Appcasestep
    extra = 0
    search_fields = ('appfindmethod')
    def delete_queryset(self,request,queryset):
        for object in queryset.filter():
            object.state =0
            object.update_time = datetime.now()
            object.save()

class AppcaseAdmin(admin.ModelAdmin):
    list_display = ['appcasename','id']
    inlines = [AppcasestepAdmin]
admin.site.register(Appcase,AppcaseAdmin)
