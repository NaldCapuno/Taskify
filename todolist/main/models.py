from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    name = models.CharField(max_length=30)
    level = models.IntegerField()

    def __str__(self):
        return self.name

class Tag(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class TaskList(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class Task(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE) 
    description = models.TextField(blank=True)
    due_date = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag, blank=True)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title