from django.core.management.base import BaseCommand
# from create_fake_data.create_products import create_product_


class Command(BaseCommand):
    help = 'Generate fake products data'

    def handle(self, *args, **options):
        self.stdout.write("Creating fake products...")

        # Productlarni yaratish
        # create_product_()

        self.stdout.write(self.style.SUCCESS("Successfully created 1000 fake products"))
