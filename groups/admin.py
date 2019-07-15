from django.contrib import admin

from .models import Group, GroupAdmin, Groupprojects, Groupuser


admin.site.register(Group)
admin.site.register(Groupuser)
admin.site.register(Groupprojects)
admin.site.register(GroupAdmin)

'''
from .models import Usrgroup, Groupdetails, Progroup
# Register your models here.

admin.site.register(Usrgroup)
admin.site.register(Groupdetails)
admin.site.register(Progroup)



'''

