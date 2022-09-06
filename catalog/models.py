from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    time_period = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')
    
    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=50, help_text="Give a title to the book")
    picture = models.ImageField(upload_to="images/", default="images/default.png", null=True, blank=True)
    author = models.ForeignKey(Author, null=True, blank=True, on_delete=models.SET_NULL)
    genre = models.ManyToManyField(Genre , verbose_name=("Genre"), related_name="books")
    
    class Meta:
        ordering = ['-id']
    
    def __str__(self):
         return self.title

    @property
    def get_image_url(self):
        try:
            return self.picture.url
        except:
            return ""