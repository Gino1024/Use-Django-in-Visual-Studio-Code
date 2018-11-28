from django.db import models

class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")
    
    def __str__(self):
      
        return f"'{self.message}' logged on {self.log_date.strftime('%A, %d %B, %Y at %X')}"