from django.db import models # Expected: Import models from django
from django.utils import timezone # Expected: Import timezone from django with timezone awareness

# Create your models here.
class Authors(models.Model): # Expected: Table called Authors class inherits from models.Model
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Books(models.Model): # Expected: Table called Books class inherits from models.Model
    title = models.CharField(max_length=200)
    authors = models.ForeignKey(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Members(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    membership_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.first_name} {self.last_name} (joined {self.membership_date.date()})"
    
class Loans(models.Model):
    members = models.ForeignKey(Members, on_delete=models.CASCADE)
    books = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrow_date = models.DateTimeField(default=timezone.now) 
    return_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.members} currently has {self.books} and was rented on {self.borrow_date.date()} and set to return on {self.return_date.date()}."