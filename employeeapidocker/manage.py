#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#from dotenv import load_dotenv
import os
import sys
import os
from dotenv import load_dotenv
load_dotenv()
ENV=os.getenv('DJANGO_ENV', 'dev')
if ENV == 'prod':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.prod')
elif ENV == 'test':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.test')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.dev')
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.dev'))
# Ensure the environment variable is set for Django settings module
def main():
    """Run administrative tasks."""
    #os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.dev')
    if ENV == 'prod':
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.prod')
    elif ENV == 'test':
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.test')
    else:
      os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'employee_api.config.settings.dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
