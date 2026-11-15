from datetime import datetime
from pathlib import Path
from urllib.parse import urlsplit

from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Pavan's Portfolio")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    theme = request.cookies.get("theme", "light")
    if theme not in ("light", "dark"):
        theme = "light"

    skills = [
        "Python",
        "SQL",
        "MySQL",
        "FastAPI",
        "HTML",
        "CSS",
        "Git",
        "Prompt Engineering",
    ]

    projects = [
        {
            "title": "Library Management System",
            "description": (
                "A Python and MySQL application to add, search, issue, "
                "and return books while tracking available quantities."
            ),
            "technologies": ["Python", "MySQL"],
            "github_url": "https://github.com/pavantejasiliveru-ai/Library-Management-System"
        },
        {
            "title": "Restaurant Billing System",
            "description": (
                "A restaurant billing application with customer registration, "
                "menu display, order management, discounts, and bill calculation."
            ),
            "technologies": ["Python", "MySQL"],
            "github_url": "https://github.com/pavantejasiliveru-ai/Restaurant_Billing"
        },
        {
            "title": "Product Display Application",
            "description": (
                "A web application that displays products and individual "
                "product details using server-side templates."
            ),
            "technologies": ["Python", "FastAPI", "Jinja2", "MySQL", "HTML", "CSS"],
            "github_url": "https://github.com/pavantejasiliveru-ai/Product-Display-Application"
        },
    ]

    profile_image_exists = Path("static/images/profile.jpeg").is_file()

    context = {
        "request": request,
        "theme": theme,
        "theme_name": "Dark" if theme == "light" else "Light",
        "skills": skills,
        "projects": projects,
        "year": datetime.now().year,
        "profile_image_exists": profile_image_exists,
    }

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context=context,
    )


@app.post("/set-theme")
async def set_theme(request: Request):
    current_theme = request.cookies.get("theme", "light")
    if current_theme not in ("light", "dark"):
        current_theme = "light"

    new_theme = "dark" if current_theme == "light" else "light"

    referer = request.headers.get("referer")
    redirect_url = "/"
    if referer:
        parsed_referer = urlsplit(referer)
        if parsed_referer.netloc == request.url.netloc and parsed_referer.scheme in ("http", "https"):
            redirect_url = parsed_referer.path or "/"
            if parsed_referer.query:
                redirect_url += f"?{parsed_referer.query}"
            if parsed_referer.fragment:
                redirect_url += f"#{parsed_referer.fragment}"

    response = RedirectResponse(url=redirect_url, status_code=303)
    response.set_cookie(
        key="theme",
        value=new_theme,
        max_age=2592000,  # 30 days
        httponly=True,
        samesite="lax",
    )
    return response
