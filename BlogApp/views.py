from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from BlogApp.models import Blogs
from BlogApp.serializers import BlogsSerializer

# Create your views here.
@csrf_exempt
def blogApi(request,id=0):
    if request.method=='GET':
        blogs= Blogs.objects.all()
        blogs_serializer=BlogsSerializer(blogs,many=True)
        return JsonResponse(blogs_serializer.data,safe=False)
    elif request.method=='POST':
        print("Hello post")
        blogs_data=JSONParser().parse(request)
        print(blogs_data)
        blogs_serializer=BlogsSerializer(data=blogs_data)
        print(blogs_serializer)
        if blogs_serializer.is_valid():
            print("saving")
            blogs_serializer.save()
            print("saved")
            return JsonResponse("Added Successfully",safe=False)    
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        blog_data=JSONParser().parse(request) 
        blog=Blogs.objects.get(id=blogs_data['id'])
        blogs_serializer=BlogsSerializer(blog,data=blog_data)
        if blogs_serializer.is_valid():
            blogs_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        blog=Blogs.objects.get(id=id) 
        blog.delect()
        return JsonResponse("Deleted Successfully",safe=False)          