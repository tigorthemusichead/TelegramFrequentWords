import requests
from .models import File
from datetime import datetime, timezone, timedelta
import os
from django.conf import settings

def filesDeleteJob():
    files = File.objects.all()
    for file in files:
        life_time = datetime.now(timezone.utc) - file.created_on
        print(life_time)
        if life_time.total_seconds() > 600:
            file_path = str(settings.MEDIA_ROOT) + "/" + file.file_name
            file.delete()
            if os.path.isfile(file_path):
                os.remove(file_path)
