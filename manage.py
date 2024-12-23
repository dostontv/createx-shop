#!/usr/bin/env python
import os
import sys

# from create_fake_data.create_categories import create_categories

# from create_fake_data.create_products import create_product_
# from create_fake_data.create_variants import create_product_variants
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
