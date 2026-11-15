# Personal Portfolio Website

A server-side rendered single-page personal portfolio built with Python, FastAPI, Jinja2, HTML, and CSS.

## Features

- Single portfolio page served from `GET /`
- Jinja2 template inheritance using `base.html` and `index.html`
- Dynamic skills and projects rendered from Python data
- Static CSS and image serving through FastAPI `StaticFiles`
- Theme preference stored in an HTTP cookie
- Dark/light theme switch through `POST /set-theme`
- HTTP 303 redirect after changing the theme
- Responsive layout for desktop and mobile screens

## Setup

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/ in your browser.

## Add your profile photo

Copy your own professional headshot to:

`static/images/profile.jpg`

The page displays initials until this file is added.

## Personalize contact links

Edit the email, GitHub, and LinkedIn placeholders in `templates/index.html` with your actual details.

## Theme cookie

The `theme` cookie is stored for 30 days with `HttpOnly` and `SameSite=Lax` settings. The theme is read on each page request; no JavaScript or localStorage is used.
