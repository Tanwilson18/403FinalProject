from django.db import models

# models (classes)


class menu(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return (self.name)

    class Meta:  # this creates a new name for the table in the database
        db_table = "new_menu"


class item(models.Model):
    menu = models.ForeignKey(menu, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return (self.name)
