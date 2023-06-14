from django.contrib import admin
from .models import User, FlashcardSet, Flashcard

# Register your models here.
admin.site.register(User)
admin.site.register(FlashcardSet)
admin.site.register(Flashcard)