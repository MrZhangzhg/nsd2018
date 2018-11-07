from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ('question_text',)
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question)
admin.site.register(Choice)
