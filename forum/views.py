from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from forum.serializers import TopicSerializerCreate, TopicSerializerGet, TopicSerializerAll, PostSerializer
from users.utilis import put_owner_in_request_data
from forum.models import Topic, Post


@api_view(['POST'])
def topic_create(request):
    request = put_owner_in_request_data(request)
    serializer = TopicSerializerCreate(data=request.data)

    if serializer.is_valid():
        if serializer.save():
            return Response({'id': serializer.instance.id}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def topic_get(request):
    topic = Topic.objects.get(id=request.data['id'])
    serializer = TopicSerializerGet(instance=topic)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
def topic_all(request):
    topics = Topic.objects.all()
    result = []
    for topic in topics:
        topic_dict = TopicSerializerAll(instance=topic).data
        topic_result = {**topic_dict, 'post_count': topic.posts.count()}
        if topic_result['post_count'] > 0:
            first_post = topic.posts.order_by('date')[0]
            serializer = PostSerializer(instance=first_post)
            topic_result['first_post'] = serializer.data

        result.append(topic_result)
    return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
def topic_remove(request):
    topic = Topic.objects.get(id=request.data['id'])
    topic.delete()
    return Response({'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_create(request):
    request = put_owner_in_request_data(request)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        if serializer.save():
            topic = Topic.objects.get(id=request.data['topic_id'])
            topic.posts.add(serializer.instance.id)
            return Response({'id': serializer.instance.id}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def post_get(request):
    post = Post.objects.get(id=request.data['id'])
    serializer = PostSerializer(instance=post)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@api_view(['POST'])
def post_remove(request):
    post = Post.objects.get(id=request.data['id'])
    post.delete()
    return Response({'OK'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def post_edit(request):
    post = Post.objects.get(id=request.data['id'])
    serializer = PostSerializer(instance=post, data=request.data)
    if serializer.is_valid():
        if serializer.save():
            return Response({'id': serializer.instance.id}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
