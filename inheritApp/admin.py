from django.contrib import admin

from inheritApp.models import StudentModel,TeacherModel,ParentModel,LaptopModel,LaptopUserModel,LocationModel,LocProxyModel


admin.site.register(StudentModel)
admin.site.register(TeacherModel)
admin.site.register(ParentModel)
admin.site.register(LaptopModel)
admin.site.register(LaptopUserModel)
admin.site.register(LocationModel)
admin.site.register(LocProxyModel)