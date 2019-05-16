from django.contrib import admin
from  webtest.models import Webcase,Webcasestep
# admin.site.register(Webcasestep)
from datetime import datetime

class WebcaseAdmin(admin.TabularInline):
    list_display = ['webcase_models','webcasename','webcasedesc','webteststep','webcase_charger','creat_time']
    model = Webcase
    extra = 1

class WebcasestepAdmin(admin.TabularInline):
    list_display = ['webtestlocation','webfindmethod','webkwargesone','webkwargestwo','webkwargesthree','webassertdata','webtestresult','webcomments','Webcase','id']
    model = Webcasestep
    extra = 0
    search_fields = ('webfindmethod')
    def delete_queryset(self,request,queryset):
        for object in queryset.filter():
            object.state =0
            object.update_time = datetime.now()
            object.save()

class WebcaseAdmin(admin.ModelAdmin):
    list_display = ['webcasename','id']
    inlines = [WebcasestepAdmin]
admin.site.register(Webcase,WebcaseAdmin)


