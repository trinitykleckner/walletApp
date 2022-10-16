from django.db import models

class Budget(models.Model):
    entertainment = models.FloatField(default=0.0)
    shopping = models.FloatField(default=0.0)
    health = models.FloatField(default=0.0)
    food = models.FloatField(default=0.0)
    transportation = models.FloatField(default=0.0)
    education = models.FloatField(default=0.0)
    bills = models.FloatField(default=0.0)
    travel = models.FloatField(default=0.0)

    def getEntertainment(self):
        return "Entertainment Budget: "+str(self.entertainment)

    def getShopping(self):
        return "Shopping Budget: "+str(self.shopping)

    def getHealth(self):
        return "Health and Fitness Budget: "+str(self.health)

    def getFood(self):
        return "Food Budget: "+str(self.food)

    def getTransportation(self):
        return "Transportation Budget: "+str(self.transportation)

    def getEducation(self):
        return "Education Budget: "+str(self.education)

    def getBills(self):
        return "Bills Budget: "+str(self.bills)

    def getTravel(self):
        return "Travel Budget "+str(self.travel)

    def __str__(self):
        out = self.getEntertainment()+"\n"+ self.getShopping()+"\n"+ self.getHealth()+"\n"+ self.getFood()+"\n"+ self.getTransportation()+"\n"+ self.getEducation()+"\n"+ self.getBills()+"\n"+self.getTravel()
        return out

        
class Spend(models.Model):
    BILLS = 'bills'
    EDUCATION = 'ed'
    ENTERTAINMENT = 'entertainment'
    FOOD = 'food'
    HEALTH = 'health'
    SHOPPING = 'shopping'
    TRANSPORTATION = 'transp'
    TRAVEL = 'travel'

    CATEGORY_CHOICES = [
        (BILLS, "Bills"),
        (EDUCATION, "Education"),
        (ENTERTAINMENT, 'Entertainment'),
        (FOOD, 'Food'),
        (HEALTH, 'Health and Fitness'),
        (SHOPPING, 'Shopping'),
        (TRANSPORTATION, 'Auto and Transportation'),
        (TRAVEL, "Travel"),
    ]

    category = models.CharField(
        max_length = 30,
        choices = CATEGORY_CHOICES
    )
    amount = models.FloatField()

    def __str__(self):
        return "You spent "+str(self.amount)+" on "+str(self.category)
