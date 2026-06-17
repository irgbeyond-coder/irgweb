from django.db import models
from django.utils.text import slugify

class Chronicle(models.Model):
    # The "Headline" of your newspaper entry
    title = models.CharField(max_length=200)
    
    # URL-friendly version of the title (e.g., "my-first-game")
    slug = models.SlugField(unique=True, blank=True)
    
    # The actual story/dev log
    content = models.TextField()
    
    # Your pixel art or retro cover
    cover_image = models.ImageField(upload_to='chronicles/', null=True, blank=True)
    
    # Date published
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Is this a "Breaking News" headline?
    is_headline = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title