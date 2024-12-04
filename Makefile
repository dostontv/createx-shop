mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

delmig:
	rm -rf apps/orders/migrations/
	rm -rf apps/products/migrations/
	rm -rf apps/users/migrations/

	mkdir apps/orders/migrations
	mkdir apps/products/migrations
	mkdir apps/users/migrations

	touch apps/orders/migrations/__init__.py
	touch apps/products/migrations/__init__.py
	touch apps/users/migrations/__init__.py

	rm -rf db.sqlite3

super:
	python3 manage.py createsuperuser

celery:
	celery -A root worker --loglevel=INFO