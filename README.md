# Inner Reality Chronicles

A Django-based storytelling and chronicle site built with a lightweight `core` app for publishing news-style posts, archive pages, and static sections.

## Overview

This project uses Django 6 and SQLite to serve a simple content site with:
- a home page showing the latest Chronicle post
- a chronicle archive listing all posts
- individual post detail pages
- static pages: About, Contact, Machines
- Django admin for managing Chronicle entries

## Features

- `Chronicle` model with title, slug, content, cover image, created date, and headline flag
- Homepage loads the latest post
- Archive page at `/chronicles/`
- Post detail pages at `/post/<pk>/`
- Easy static pages for About, Contact, and Machines
- SQLite database ready for local development

## Tech Stack

- Python 3.14
- Django 6.0.2
- Pillow for image fields
- python-dotenv for environment configuration
- SQLite database

## Getting Started

### 1. Activate virtual environment

From the repository root:

```bash
source .venv/bin/activate
```

### 2. Install dependencies

If you do not have a `requirements.txt`, install the main dependencies directly:

```bash
python -m pip install django pillow python-dotenv
```

### 3. Move into the Django project directory

```bash
cd src
```

### 4. Create a `.env` file

Create `src/.env` with at least these values:

```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Create a superuser

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Admin

Visit `http://127.0.0.1:8000/admin/` to log in and manage Chronicle entries.

## Project Structure

- `src/manage.py` — Django management entry point
- `src/innerreality_config/` — project settings and URL config
- `src/core/` — main Django app with models, views, templates, and static files
- `src/db.sqlite3` — SQLite development database

## Notes

- The app uses the `core` Django app for page logic and the `Chronicle` model.
- If you add file uploads or serve media files, you may need to configure `MEDIA_URL` and `MEDIA_ROOT` in `innerreality_config/settings.py`.

