from django.contrib import admin

from .models import Snippet

class SnippetModelAdmin(admin.ModelAdmin):	
	class Meta:
		model = Snippet

admin.site.register(Snippet, SnippetModelAdmin)

