from django.db import models

class Admin(models.Model):
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    head       = models.CharField(max_length=300)
    hits       = models.IntegerField()
    user_post  = models.OneToOneField('users.User', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'admins'