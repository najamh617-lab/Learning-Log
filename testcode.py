import os
import django

# Point Python at your project's settings, then load Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'learning_log.settings')
django.setup()

# Imports from your app must come AFTER django.setup()
from MainApp.models import Topic, Entry

# All topics
topics = Topic.objects.all()
for topic in topics:
    print(topic.id, topic)

# One topic by id
t = Topic.objects.get(id=1)
print(t.text)
print(t.date_added)

# All entries for that topic (through the foreign key)
for entry in t.entry_set.all():
    print(entry)

from django.contrib.auth.models import User

for user in User.objects.all():
    print(user.username, user.id)