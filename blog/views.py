from django.views.generic.list import ListView
from pipes import Template
from re import template
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post, Contact
from .forms import AddForm, CommentForm

# about page


def about(request):
    return render(request, '../templates/blog/about.html')

# contact page


def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.phone = phone
        contact.message = message
        contact.save()
    return render(request, '../templates/blog/contact.html')

# Create


def create_view(request):

    context = {}

    form = AddForm(request.POST or None, initial={'author': request.user.id})
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "add_post.html", context)


# update/edit


def update_view(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('/')
    if post_sel.author == request.user:
        post_form = AddForm(request.POST or None, instance=post_sel)
        if post_form.is_valid():
            post_form.save()
            return redirect('/')
        context = {}  
        context['form'] = post_form
        return render(request, 'update_view.html', context)
    else:
        return redirect("/")

# delete


def delete_view(request, post_id):
    post_id = int(post_id)
    try:
        post_sel = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return redirect('home')
    if post_sel.author == request.user:
        post_sel.delete()
    return redirect('home')

# 404 ERROR HANDLER


def custom_view(request):
    return render(request, '500.html')


def custom_view(request, exception):
    return render(request, '404.html', status=404)


def error404_page(request):
    return render(request, '../templates/blog/404.html')


def error505_page(request):
    return render(request, '../templates/blog/505.html')

# search results invalid search to respond with 404 template


def get_queryset(request):
    query = request.GET.get("q")
    if query:
        object_list = Post.objects.filter(ingredients__icontains=query)
        return render(request, 'blog/search_results.html', {'object_list': object_list})
    else:
        return render(request, '404.html')

# post list amount on website page 6


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


# Blog post Detail inluding liking/ commenting

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
