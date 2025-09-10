from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class AuthorModel(BaseModel):
    full_name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    bio = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Author'
        verbose_name_plural='Authors'

class ContactModel(BaseModel):
    full_name = models.CharField(max_length=128)
    email = models.EmailField()
    phone_number = models.CharField(
        max_length=15,
        null = True ,blank=True
    )
    subject = models.CharField(
        max_length=255, null=True, blank=True
    )
    message = models.TextField()

    is_read = models.BooleanField(default=False)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"

    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'

class AboutModel(BaseModel):
    title = models.CharField(max_length=127)
    image = models.ImageField(upload_to='About/')
    content = models.TextField()
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE,related_name='blogs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='About'
        verbose_name_plural='Abouts'