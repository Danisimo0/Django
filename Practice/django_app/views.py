from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from .models import Post, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[pk]))
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'form': form})


class CommentView(View):
    form_class = CommentForm
    template_name = 'blog/comment_list.html'

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = post.comments.all()
        form = self.form_class()
        return render(request, self.template_name, {'post': post, 'comments': comments, 'form': form})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]


class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
