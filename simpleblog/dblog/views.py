# -*- coding: utf-8 -*-

"""Django view classes for a simple Blog site

   This example shows several simple views that retrieve
   the appropriate objects, populate a template context
   and then render the template.
"""

from django.shortcuts import render_to_response, get_object_or_404
from simpleblog.dblog.models import Blog
from django.http import HttpResponseRedirect
from datetime import datetime

def index(request):
    """Generate the context for the main summary page"""
    latest_blog_list = Blog.objects.all().order_by('-post_date')[:3]
    return render_to_response('templates/index.html', 
                              {'latest_blog_list': latest_blog_list})

def readBlog(request, blog_id):
    """Generate the context for the page that displays a single
       blog entry"""
    blog = get_object_or_404(Blog, pk=blog_id)
    return render_to_response('templates/readBlog.html', {'blog': blog})

def comment(request, blog_id):
    """Generate the context for the page that displays the comments
       for a particular blog entry"""
    blog = get_object_or_404(Blog, pk=blog_id)
    return render_to_response('templates/comment.html', 
                              {'comments': blog.comment_set.all(),
                               'blog': blog}
                              )

def addComment(request, blog_id):
    """Generate the context for the form in which new comments
       are entered"""
    blog = get_object_or_404(Blog, pk=blog_id)
    return render_to_response('templates/addComment.html', {'blog': blog})

def writeBlog(request):
    """No context for this page.  Just render the template"""
    return render_to_response('templates/blogEntry.html')

def postEntry(request):
    """Accepts the HTTP POST data of a new blog entry and 
       updates the database accordingly"""
    b = Blog()
    b.title = request.POST['title']
    b.reply_to = request.POST['reply_to']
    b.content = request.POST['content']
    b.post_date = datetime.now()
    b.save()
    return HttpResponseRedirect('/simpleblog/blog/%s/' % b.id)

def postComment(request, blog_id):
    """Accepts the HTTP POST data of a new blog comment and updates
       the database accordingly"""
    blog = get_object_or_404(Blog, pk=blog_id)
    comment = blog.comment_set.create(content=request.POST['content'], 
                                      rating=request.POST['rating'])
    comment.save()
    return HttpResponseRedirect('/simpleblog/blog/%s/comment' % blog.id)
