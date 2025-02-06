import os
import uuid

from django.conf import settings
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        file_obj = request.FILES['file']
        file_name_suffix = file_obj.name.split(".")[-1]
        if file_name_suffix not in ["jpg", "png", "gif", "jpeg", ]:
            return JsonResponse({"message": "错误的文件格式"})

        upload_time = timezone.now()
        path = os.path.join(
            settings.MEDIA_ROOT,
            'tinymce',
            str(upload_time.year),
            str(upload_time.month),
            str(upload_time.day)
        )
        # 如果没有这个路径则创建
        if not os.path.exists(path):
            os.makedirs(path)
        new_file_name = '{}.{}'.format(uuid.uuid4().hex[:10], file_name_suffix)
        file_path = os.path.join(path, new_file_name)

        file_url = f'{settings.MEDIA_URL}tinymce/{upload_time.year}/{upload_time.month}/{upload_time.day}/{new_file_name}'

        if os.path.exists(file_path):
            return JsonResponse({
                "message": "文件已存在",
                'location': file_url
            })

        with open(file_path, 'wb+') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)

        return JsonResponse({
            'message': '上传图片成功',
            'location': file_url
        })
    return JsonResponse({'detail': "错误的请求"})
