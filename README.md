#  :snake:Django + :heavy_check_mark:Vue + :large_blue_diamond:Webpack + :gear:.env

## Story
I was searching for an example/template for combining django+vue+webpack. Althought there are many repos and posts on it, none of them covered different environments settings, multiplie pages, switching hotreload. Most of them used old vue-cli config. So I combined all that exmaples and added support for multiplie pages and .env settings.
If you know how to make it better, plase feel free to contribute.

## Intallation

It is supposed that you have installed:
- python 3.6+ (https://www.python.org/downloads/) 
- pipenv (`pip install --user pipenv`)
- node + npm (https://nodejs.org/en/)
- vue-cli 3 (`npm install -g @vue/cli`)

```bash
# Clone the repo
git clone https://github.com/rguliev/django-vue-webpack-template.git
cd django-vue-webpack-template

# Set your env
cp .env.example .env 

# Install all backend dependencies
cd backend
pipenv install
python manage.py makemigrations
python manage.py migrate

# Install all frontend dependencies
cd ../frontend
npm install
```

## Run dev with hot-reload
1. Set both django and node env to development:
```
DJANGO_ENV=development
NODE_ENV=development
```
2. run in terminal: `cd frontend && npm run serve`
3. run **in another** terminal: `cd backend && python manage.py runserver`
4. Open http://127.0.0.1:8000/

## Run dev without hot-reload
1. Set django to development and node to production:
```
DJANGO_ENV=development
NODE_ENV=production
```
2. run in terminal: 
```bash
cd frontend
npm run build
cd ../backend
python manage.py runserver
```
3. Open http://127.0.0.1:8000/

## Related sources and repos:
- A post and https://blog.gundammc.com/vue-js-django/ and the repo https://github.com/gundamMC/vue-django-multipage-example
- https://github.com/gtalarico/django-vue-template
- https://medium.com/@michealjroberts/part-1-integrating-django-2-vue-js-and-hot-webpack-reload-setup-387a975166d3
- https://github.com/phpdude/docker-django-webpack-skeleton

