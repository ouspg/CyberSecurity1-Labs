from flask import Blueprint, render_template, request

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

USERS = {
    "admin": "password123",  # Weak password for brute forcing
}

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    flag = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if USERS.get(username) == password:
            return render_template("secret.html")

    return render_template("login.html")


