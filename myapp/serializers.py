# myapp/serializers.py
from rest_framework import serializers
from .models import UploadedImage

class UploadedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedImage
        # 如果你希望在响应或写入时也能使用 custom_folder，就把它加进来
        fields = ['id', 'image', 'upload_time', 'custom_folder']
        # 也可以只读：
        # extra_kwargs = {
        #     'custom_folder': {'read_only': True}
        # }
