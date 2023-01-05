from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator

# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='Hi my name is ... my trying to improve, create, learn, build', max_length=355)
    user_image = models.ImageField(default='default-avatar.png', upload_to='media', validators=[FileExtensionValidator(['png', 'jpg'])])

    def __str__(self) -> str:
        return f'profile of{self.user.username}'

class PostModel(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = RichTextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    date_stamp = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    class Meta:
        ordering = ['-date_stamp']

    def total_likes(self):
        return self.likes.count()

    def comment_cout(self):
        return self.commentmodel_set.all().count()

    def comments(self):
        return self.commentmodel_set.all()

    def __str__(self) -> str:
        return self.content

class CommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = RichTextField()

    def __str__(self) -> str:
        return self.content