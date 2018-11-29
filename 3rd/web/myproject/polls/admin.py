from django.contrib import admin
from .models import Question,Choice,User
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldssets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

inlines = [ChoiceInline]
list_display = ('question_text', 'pub_date')
admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(User) # need to register then you can add/remove/update data