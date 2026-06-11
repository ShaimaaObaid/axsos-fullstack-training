from django.db import models
from datetime import date


# Create your models here.
class ShowManager(models.Manager):
    # Added show_id=None to allow exclusion during edits
    def validator(self, postData, show_id=None):
        errors = {}

        # TITLE
        if not postData.get('title') or len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"

        # NETWORK
        if not postData.get('network') or len(postData['network']) < 3:
            errors['network'] = "Network must be at least 3 characters"

        # DESCRIPTION (optional but if exists >=10)
        desc = postData.get('description', '')
        if desc and len(desc) < 10:
            errors['description'] = "Description must be at least 10 characters"

        # RELEASE DATE
        if not postData.get('release_date'):
            errors['release_date'] = "Release date is required"
        else:
            try:
                input_date = date.fromisoformat(postData['release_date'])
                if input_date > date.today():
                    errors['release_date'] = "Release date must be in the past"
            except (ValueError, TypeError):
                errors['release_date'] = "Invalid date format"

        # UNIQUENESS (Sensei bonus)
        if postData.get('title'):
            existing = self.filter(title=postData['title'])
            
            # CRITICAL FIX: If editing, ignore the show currently being updated
            if show_id:
                existing = existing.exclude(id=show_id)
                
            if existing.exists():
                errors['title'] = "A show with this title already exists"

        return errors


class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = ShowManager()

    def __str__(self):
        return self.title