#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from google.oauth2 import service_account

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:/Users/jadri/Downloads/proyectobda2-65742135074f.json"


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')
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
