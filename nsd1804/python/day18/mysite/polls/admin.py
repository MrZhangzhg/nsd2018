from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'publish_date')
    list_filter = ('publish_date',)
    date_hierarchy = 'publish_date'

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')

# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
