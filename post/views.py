import json
from turtle import title

from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt

from post.models import Post

# Create your views here.
class PostController:
    @csrf_exempt
    def index(request):
        response = 'invalid method'
    
        # get list
        if request.method == 'GET':
            response = list(Post.objects.all().values())

        # create
        elif request.method == 'POST':
            payload = json.loads(request.body)

            post = Post(
                title = payload['title'],
                content = payload['content']
            )
            post.save()

            response = model_to_dict(post)

        return HttpResponse(json.dumps(response, default=str), content_type='text/json')

    @csrf_exempt
    def detail(request, post_id):
        response = 'invalid method'
        post = Post.objects.get(id=post_id)

        # get / show
        if request.method == 'GET':
            response = model_to_dict(post)

        # update
        elif request.method == 'PUT':
            payload = json.loads(request.body)

            post.title = payload['title']
            post.content = payload['content']
            post.save()

            response = model_to_dict(post)

        # delete
        elif request.method == 'DELETE':
            response = model_to_dict(post)
            post.delete()

        return HttpResponse(json.dumps(response, default=str), content_type='text/json')