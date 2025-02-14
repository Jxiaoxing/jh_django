from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import UploadedImage
from .serializers import UploadedImageSerializer

class ImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        # 从请求中获取自定义文件夹名
        folder_name = request.data.get('name', '')

        # 一次性取出所有同名文件
        images = request.FILES.getlist('image')  # 多张图片都在这个列表里
        if not images:
            return Response({"message": "未收到任何图片文件"}, status=400)

        saved_data = []
        for img in images:
            # 对每个图片都创建一条 UploadedImage 记录
            serializer = UploadedImageSerializer(data={
                'custom_folder': folder_name,
                'image': img
            })
            # 校验并保存
            if serializer.is_valid():
                serializer.save()  # 会在 models.py 里使用 upload_to 指定目录
                saved_data.append(serializer.data)
            else:
                # 如果某一张图片保存失败，可直接返回报错
                return Response(
                    {"message": "图片上传失败", "errors": serializer.errors},
                    status=400
                )

        return Response({"message": "图片上传成功", "data": saved_data}, status=200)