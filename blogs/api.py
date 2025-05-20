from ninja import Router
from .models import Blog
from typing import List
from pydantic import BaseModel
from django.shortcuts import get_object_or_404

blogRouter = Router()

class BlogSchema(BaseModel):
    title: str
    content: str
    author: str

@blogRouter.get("/", response=List[BlogSchema])
def list_blogs(request):
    return list(Blog.objects.values("title", "content", "author"))

@blogRouter.post("/")
def create_blog(request, payload: BlogSchema):
    blog = Blog.objects.create(**payload.dict())
    return {"id": blog.id, "message": "Blog created successfully!"}

@blogRouter.get("/{blog_id}", response=BlogSchema)
def get_blog(request, blog_id: int):
    blog = get_object_or_404(Blog, id=blog_id)
    return {"title": blog.title, "content": blog.content, "author": blog.author}

@blogRouter.put("/{blog_id}")
def update_blog(request, blog_id: int, payload: BlogSchema):
    blog = get_object_or_404(Blog, id=blog_id)
    for key, value in payload.dict().items():
        setattr(blog, key, value)
    blog.save()
    return {"message": "Blog updated successfully!"}

@blogRouter.delete("/{blog_id}")
def delete_blog(request, blog_id: int):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return {"message": "Blog deleted successfully!"}
