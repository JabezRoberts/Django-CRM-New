from django.db import models
from django.contrib.auth.models import AbstractUser

# models are a representation of our database schema
# Create your models here.


class User(AbstractUser):
    pass
    
    
    
class Lead(models.Model):
    
    """
    SOURCE_CHOICES = (
        ('YouTube', 'YouTube'),
        ('Google', 'Google'),
        ('Newsletter', 'Newsletter')
    )
    phoned = models.BooleanField(default=False)
    source = models.CharField(choices=SOURCE_CHOICES, max_length=100) # a dropdown menu with choices to choose fro,
    
    profile_picture = models.ImageField(blank=True, null=True) # blank=true means not required in forms, null=true means it can be empty in the database
    special_files = models.FileField(blank=True, null=True)
    
    """
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    
    # Now for creating relationships between models or tables
    # An agent can have many leads, but a lead can only have one agent. This is done with a foriegn key to
    # link the two tables together
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE) # this is placed on the Lead model because a lead can only have one agent
    # if it were placed on the Agent model, an agent could only have one lead
    # on_delete=models.CASCADE means if the agent is deleted, all their leads will be deleted too
    # on_delete=models.SET_NULL, null=True means if the agent is deleted, the lead's agent will be set to null
    # on_delete=models.SET_DEFAULT, default=1 means if the agent is deleted, the lead's agent will be set to the agent with id 1
    
    # Lead won't be associated with a user because it is a record of a potential customer, not a user of the system
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) #models.OneToOneField means one user can only be linked to one agent, models.ForeignKey means one user can be linked to many agents
    # User already has username, password, email, first_name, last_name fields because it inherits from AbstractUser

    """
    to change the output from "agent = Agent.objects.create(user=admin_user)
    agent <Agent: Agent object (1)>:" to something more meaningful and english-like
    """
    def __str__(self):
        return self.user.email