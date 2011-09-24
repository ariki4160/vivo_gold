from django.conf.urls.defaults import *
from models import Note

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic.list_detail import object_list

from forms import NoteForm
from views import post_note

urlpatterns = patterns('',
    url(r'post_note/$', post_note, name='post_note'),
    (r'$', object_list, dict(queryset=Note.objects.all().order_by('-id').select_related(depth=1),
                            paginate_by=20, extra_context=dict(form=NoteForm())), 'microblog_home'),
)
