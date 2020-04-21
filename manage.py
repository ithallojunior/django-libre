#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'store.settings')
    try:
        # overriding to be possible to set default port and ip
        from django.core.management.commands.runserver import Command as runserver
        runserver.default_addr = '127.0.0.1' # must be added to the ALLOWED_HOSTS
        runserver.default_port = '8000'

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
