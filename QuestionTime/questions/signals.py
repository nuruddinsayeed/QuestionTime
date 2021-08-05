from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from questions.models import Question


@receiver(pre_save, sender=Question)
def add_slug_to_question(sender, instance, *args, **kwargs):
    """Because of pre_save singal it will be called every time before
        Questions object updated or created and here instance is the
        Questions instance that is going to be created or updated"""

    if instance and not instance.slug:
        slug = slugify(instance.content)
        random_string = generate_random_string()

        # this slug will be saved in our question instance
        instance.slug = slug + "-" + random_string

# pre_save.connect(add_slug_to_question, sender=Question)