from django.db import models

# Create your models here.
class Article(models.Model):
    # 博客题目
    title = models.CharField(max_length = 100)
    # 博客标签
    category = models.CharField(max_length = 500, blank = True)
    # 博客日期
    date_time = models.DateTimeField(auto_now_add = True)
    # 博客文章正文
    content = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']