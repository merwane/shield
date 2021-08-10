from mongoengine import *
import datetime

class UniqueFile(Document):
    filename = StringField()
    file_size = FloatField(default=0) # megabytes by default
    file_type = StringField()
    labels = ListField(default=[])
    added_at = DateTimeField(default=datetime.datetime.utcnow)