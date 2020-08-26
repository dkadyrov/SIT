from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# Look up Table? 
accessibility = { 
    "high-contrast": 1, 
}

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     preferences = models.CharField("Accessibility", max_length=255, blank=True, null=True)
#     # TODO
#     # Or we do boolean and list every trait of the profile...
    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

class Art(models.Model):
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(
        "Created At", auto_now_add=True)    
    image_1 = models.ImageField(upload_to='images/')
    image_2 = models.ImageField(upload_to='images/')
    filepath = models.ImageField(upload_to='images/', null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    number = models.IntegerField(default=1)

    def __str__(self):
        return self.title

    def publish(self):
        self.date_created = timezone.now()
        self.save()

class Like(models.Model):
    art = models.ForeignKey(
        Art, related_name='liked_post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liker',
                             on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} : {}'.format(self.user, self.art)
