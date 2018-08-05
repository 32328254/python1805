from django.contrib import admin

# Register your models here.

#将某型导入
from .models import Question,Choice

"""
将某型注册到管理界面
"""

admin.site.register(Question)
admin.site.register(Choice)
