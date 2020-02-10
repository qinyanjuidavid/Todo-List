from django.db import models



class Todo(models.Model):
    event=models.CharField(max_length=20000,unique=True)
    time_added=models.DateTimeField(auto_now_add=True)
    time_updated=models.DateTimeField(auto_now=True)
    done=models.BooleanField(default=False)
    #event_time=models.DateTimeField()


    def __str__(self):
        return self.event
