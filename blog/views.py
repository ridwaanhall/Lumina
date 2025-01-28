from django.shortcuts import render
from django.views import View
from django.utils.text import slugify

from . import blog_data


class BlogListView(View):
    def get(self, request):
        blogs = blog_data.BlogData.blogs

        context = {
            'blogs': blogs
        }
        return render(request, 'blog/blog.html', context)

class BlogDetailView(View):
    def get(self, request, title):

        blogs = blog_data.BlogData.blogs

        blog_post = next((item for item in blogs if slugify(item['title']) == title), None)
        other_blogs = [item for item in blogs if slugify(item['title']) != title]

        if blog_post:
            context = {
                'blog' : blog_post,
                'other_blogs': other_blogs
            }
            return render(request, 'blog/blog_detail.html', context)
        else:
          return render(request, 'blog/blog_not_found.html', status=404)