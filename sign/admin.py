from django.contrib import admin
from sign.models import SignModel,SignalModel,LinkModel
# ,Task,Taskdate,Archive

admin.site.register(SignModel)
admin.site.register(SignalModel)
admin.site.register(LinkModel)
# admin.site.register(Task)
# admin.site.register(Taskdate)
# admin.site.register(Archive)