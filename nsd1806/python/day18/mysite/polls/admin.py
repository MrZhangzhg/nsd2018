from django.contrib import admin
from .models import Question, Choice

# admin.site.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_text', 'pub_date']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'
    search_fields = ['question_text']
    ordering = ['-pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
