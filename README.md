This is a Django backend for my personal website, hosted on AWS Lambda. It uses the serverless framework and zappa to deploy the Django app to AWS Lambda. The frontend is a static website hosted on S3. This tutorial was very helpful: 
https://www.davur.net/pages/django-on-aws-lambda/

to add static files:
`python manage.py collectstatic --noinput `