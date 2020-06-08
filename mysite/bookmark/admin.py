from django.contrib import admin

# Register your models here.
from bookmark.models import Bookmark

# 모델을 관리자 페이지에 등록
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    # 화면에 보여줄 항목들을 정의
    list_display = ('id', 'title', 'url', 'description')