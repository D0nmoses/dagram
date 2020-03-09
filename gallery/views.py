from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Follow, Like, Comment, Post, Profile
# Create your views here.

@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user

    title = 'Home'

    following = Follow.get_following(current_user.id)

    posts = Post.get_posts()

    comments = Comment.get_post_comments(posts.id)

    following_posts = []

    for follow in following:

        for post in posts:

            if follow.profile == post.profile:
                following_posts.append(post)

    return render(request, 'all-gram/home.html',
                  {"comments":comments, "title": title, "following": following, "user": current_user, "posts": posts, "following_posts": following_posts})
