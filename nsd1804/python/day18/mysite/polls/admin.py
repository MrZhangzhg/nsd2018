from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'publish_date')
    list_filter = ('publish_date',)
    date_hierarchy = 'publish_date'
    search_fields = ('question_text',)
    ordering = ('-publish_date', 'question_text')

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    raw_id_fields = ('question',)

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
