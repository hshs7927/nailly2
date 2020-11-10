from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
#user은 아무이름이나 붙여도 된다. 포린키는 author와달리 이름그대로 쓰이는게아니다. 
# author = models.CharField(max_length=100) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    body = models.TextField()
    image = models.ImageField(upload_to='posts', null=True)
    created_at = models.DateTimeField()
    liked_users = models.ManyToManyField(User, related_name='liked_posts')

    def __str__(self):
        if self.user:
            return f'{self.user.get_username()}: {self.body}'
        return f'{self.body}'