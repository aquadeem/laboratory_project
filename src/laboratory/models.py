from django.db.models import Model, CharField, DateTimeField


class DateTimeMixin(Model):
    created_at = DateTimeField(auto_now_add=True, null=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Student(DateTimeMixin, Model):

    first_name = CharField(max_length=50)
