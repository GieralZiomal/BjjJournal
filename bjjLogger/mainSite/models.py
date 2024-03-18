from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User


TYPE_CHOICES = {
    "no-gi": "NO-GI",
    "gi": "GI",
}

FIGHT_CHOICES = {
    "Win": "W",
    "Lose": "L",
}

END_CHOICES = {
    "Submission": "SUB",
    "Points": "PO",
    "Disqualification": "DQ",
    "Choice": "CHO",
}


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, date_of_birth, password, belt):
        if not email:
            raise ValueError("Users must have an email address")

        # Sprawdź, czy nazwa użytkownika jest unikalna
        if MyUser.objects.filter(username=username).exists():
            raise ValueError("This username is already taken")

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            username=username,
            belt=belt,
        )

        user.set_password(password)
        user.save(using=self._db)
        user.is_active = False
        return user

    def create_superuser(self, email, username, date_of_birth, password=None):
        user = self.create_user(
            email=email,
            username=username,
            date_of_birth=date_of_birth,
            password=password,
            belt="Admin",  # Update this with your admin belt value
        )
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user



class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="Email",
        max_length=255,
        unique=True,
    )
    username = models.CharField(
        verbose_name="Username",
        max_length=100,
        unique=True,
    )

    BELT_CHOICES = [
        ("White", "White"),
        ("Blue", "Blue"),
        ("Purple", "Purple"),
        ("Brown", "Brown"),
        ("Black", "Black"),
        ("Red", "Red"),
    ]

    belt = models.CharField(verbose_name="User Belt", choices=BELT_CHOICES, max_length=10)
    
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "date_of_birth"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Trening(models.Model):
    owner = models.ForeignKey(MyUser, related_name='training', on_delete=models.CASCADE)
    dateOfTraining = models.DateField()
    hourOfTraining = models.TimeField()
    trainingDuration = models.IntegerField()
    typeOfWorkout = models.CharField(max_length=5, choices=TYPE_CHOICES)
    howManyFights = models.IntegerField()
    fightDuration = models.IntegerField()
    breakDuration = models.IntegerField()
    tiredAfter = models.IntegerField()
    injuriesAfter = models.CharField(max_length=10)
    
    class Meta:
        ordering = ['-dateOfTraining']


class Zawody(models.Model):
    comp_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(MyUser, related_name='competition', on_delete=models.CASCADE)
    nameOfComp = models.CharField(max_length=20)
    dateOfComp = models.DateField()
    place = models.IntegerField()

    class Meta:
        ordering = ['-dateOfComp']


class CompFight(models.Model):
    owner = models.ForeignKey(MyUser, related_name='compFight', on_delete=models.CASCADE)
    whichComp = models.ForeignKey(Zawody, related_name='comp_fights', on_delete=models.CASCADE)
    resultOfFight = models.CharField(max_length=10, choices=FIGHT_CHOICES)
    endOfFight = models.CharField(max_length=20, choices=END_CHOICES)
