from django.contrib import admin
from .models import Provider
from .models import Course

class ProviderAdmin(admin.ModelAdmin):
  list_display = ('id', 'providerName', 'providerUrl', 'Email', 'Password')
  
class CourseAdmin(admin.ModelAdmin):
  list_display = ('courseProviderID','GetProviderName', 'courseName', 'authorName', 'courseUrl', 'courseSummary', 'courseCategory', 'isDownloaded')

  # Return Provider Name based on FK Provider ID
  def GetProviderName(self, obj):
    return obj.providerID.providerName
  GetProviderName.short_description = 'providerName'
  GetProviderName.admin_order_field = 'course__providerID'
  
# Register your models here.
admin.site.register(Provider, ProviderAdmin)
admin.site.register(Course, CourseAdmin)