from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import render
# from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from django_api import models
from django_api import serializers as django_serializers


def index(request):
    data = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }
    # return HttpResponse("<h1>Hello world</h1>")
    # return JsonResponse(data={
    #     "userId": 1,
    #     "id": 1,
    #     "title": "delectus aut autem",
    #     "completed": False
    # }, safe=False, content_type="application/json", indent=2)
    return JsonResponse(data=data, safe=True)


@api_view(http_method_names=["GET", "PUT", "PATCH", "DELETE"])
@permission_classes((permissions.AllowAny,))
def posts_one(request: HttpRequest, id="0") -> Response:
    id = int(id)
    try:
        post = models.Posts.objects.get(id=id)
        if request.method == "GET":
            try:
                datas = []
                data = models.Posts.objects.filter(user_id=id)  # TODO QuerySet != JSON
                for one_data in data:
                    datas.append({
                        "userId": one_data.user_id,
                        "id": one_data.id,
                        "title": one_data.title + str(" banana"),
                        "completed": one_data.completed,
                    })
                print(datas)
                return Response(data=datas, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(data={"error": f"Данных не существует"}, status=status.HTTP_204_NO_CONTENT)
        elif request.method in ["PUT", "PATCH"]:
            message = "Without changes"
            id = request.data.get("id", None)
            title = request.data.get("title", None)
            completed = request.data.get("completed", None)

            if id is None:
                return Response(data={"error": f"При обновлении не был указан id"}, status=status.HTTP_204_NO_CONTENT)
            else:
                post = models.Posts.objects.get(id=id)
                if post.title != title and title is not None:
                    post.title = title
                    message = "Successfully update"
                if post.completed != completed and completed is not None:
                    post.title = completed
                    message = "Successfully update"
                post.save()

                return Response(data={"detail": "Successfully update"}, status=status.HTTP_200_OK)

        elif request.method == "DELETE":
            post.delete()

            return Response(data={"detail": "Successfully deleted"}, status=status.HTTP_200_OK)
    except Exception as e:
        print(e, ' ошибка')
        return Response(data={"error": f"Данных не существует"}, status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=["GET", "POST"])
@permission_classes((permissions.AllowAny,))
def posts(request: HttpRequest) -> Response:
    if request.method == "GET":
        data = models.Posts.objects.all()  # TODO QuerySet != JSON
        data_json = django_serializers.PostsSerializer(instance=data, many=True)
        return Response(data=data_json.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        user_id = 0

        title = request.data.get("title", None)
        print(title)
        completed = request.data.get("completed", False)

        if title is None:
            return Response(data={"detail": "Not successfully created"}, status=status.HTTP_204_NO_CONTENT)

        new_data_in_db = models.Posts.objects.create(
            user_id=user_id,
            title=title,
            completed=completed
        )
        # Content
        {
            "title": "text"
        }
        id_in_db = new_data_in_db.id
        new_data_in_db.user_id = id_in_db // 10 + 1
        new_data_in_db.save()
        return Response(data={"detail": "Successfully created"}, status=status.HTTP_200_OK)
