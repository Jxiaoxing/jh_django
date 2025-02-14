# myapp/models.py
from django.db import models

# 用于动态构建上传路径
def user_directory_path(instance, filename):
    """
    file 最终会被上传到:
      MEDIA_ROOT/images/<custom_folder>/<filename>
    如果 custom_folder 为空, 可以设置一个默认文件夹
    """
    folder_name = instance.custom_folder if instance.custom_folder else 'default'
    return f'images/{folder_name}/{filename}'

class UploadedImage(models.Model):
    # 新增一个字段来保存文件夹名称
    custom_folder = models.CharField(max_length=100, blank=True, default='')

    # 通过 upload_to 指定动态路径
    image = models.ImageField(upload_to=user_directory_path)

    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.name
