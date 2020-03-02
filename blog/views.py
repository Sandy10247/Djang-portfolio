from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
# Lists all Blogs
def all_blogs(request):
    blogs = Blog.objects.all()
    # content
    content = {'blogs': blogs}
    return render(request, 'blog/all_blogs.html', context=content)

def detailBlog(request, blog_id):
    print("Id :- {}".format(blog_id))
    # fetching Blog by Id
    blogItem = get_object_or_404(Blog, pk=blog_id)
    # content
    content = {'blogItem': blogItem}
    return render(request, 'blog/detailBlog.html', context=content)
