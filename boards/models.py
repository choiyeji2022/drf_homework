from django.db import models
from user.models import User

class Board(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content= models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now= True)
    is_complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.title)