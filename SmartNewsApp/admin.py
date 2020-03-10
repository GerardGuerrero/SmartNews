from django.contrib import admin
from apps.blog.models import News, Source, Topic, Country, Date, Statistic

class NewsAdmin(admin.ModelAdmin):
 	pass

class SourceAdmin(admin.ModelAdmin):
 	pass

class TopicAdmin(admin.ModelAdmin):
 	pass

class CountryAdmin(admin.ModelAdmin):
 	pass

class DateAdmin(admin.ModelAdmin):
 	pass

class StatisticAdmin(admin.ModelAdmin):
 	pass

admin.site.register(News, NewsAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(Statistic, StatisticAdmin)
