from django.contrib import admin
from .models import Questions,Quiz,Quiz_Taken,Answer

admin.site.register(Quiz_Taken)
admin.site.register(Quiz)
admin.site.register(Answer)
admin.site.register(Questions)

# # from .models import Quiz,Questions,MCQ,FIB,UserAnswers

# # admin.site.register(Quiz)
# # admin.site.register(MCQ)
# # admin.site.register(FIB)

# class UserAnswerAdmin(admin.ModelAdmin):
#     list_display = ['user','question','answer']

# admin.site.register(UserAnswers,UserAnswerAdmin)

# class QuestionModel(admin.ModelAdmin):
#     list_display = ['quiz','question_name']

# admin.site.register(Questions,QuestionModel)
