from flask import Blueprint, render_template


main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

@main_bp.route("/sitemap.xml")
def sitemap():

    # TODO: add flag
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>http://localhost:5000/secret</loc>
        <flag>some flag</flag>
    </url>
</urlset>
"""
