from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.
class ImPfle(models.Model):
	g=[('Male','Male'),('Female','Female')]
	add = [('Amaravathi','Amaravathi'),('Bantumilli','Bantumilli'),('Bhimavaram','Bhimavaram'),('Eluru','Eluru'),('Gudivada','Gudivada'),('Gudlavalleru','Gudlavalleru'),('Machilipatnam','Machilipatnam'),('Kakinada','Kakinada'),('Kurnool','Kurnool'),('Kadapa','Kadapa'),('Rajahumandry','Rajahumandry'),('Sriharikota','Sriharikota'),('Vijayawada','Vijayawada'),('Vizag','Vizag')]
	u = models.OneToOneField(User,on_delete=models.CASCADE)
	im = models.ImageField(upload_to="Profile/",null=True,default="blank-profile-picture.png")
	Address = models.CharField(choices=add,max_length=15,null=True)
	date_of_birth = models.DateField(null=True)
	mb = models.CharField(max_length=10)
	gender=models.CharField(max_length=10,choices=g)

@receiver(post_save,sender=User)
def Crtpfle(sender,instance,created,**kwrgs):
	if created:
		ImPfle.objects.create(u=instance)
