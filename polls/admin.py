from django.contrib import admin
from .models import Question
from .models import Choice
# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3






class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question']}),
        ('Date infomation', {'fields':['pub_date']})

    ]
    search_fields = ['question']
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    list_display = ('question', 'pub_date', 'was_published_recently')
admin.site.register(Question, QuestionAdmin)

