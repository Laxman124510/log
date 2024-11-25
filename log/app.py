from flask import Flask, render_template, redirect, url_for, request, session
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = "supersecretkey"
login_manager = LoginManager()
login_manager.init_app(app)

# Mock database for users, roles, and permissions
users_db = {
    "kesava": {"password": "kesava123", "role": "manager"},
    "laxman": {"password": "laxman143143", "role": "admin"},
}

roles_permissions = {
    "admin": ["view_dashboard", "edit_users", "delete_users"],
    "manager": ["view_dashboard", "edit_users"],
    "viewer": ["view_dashboard"],
}

# User class
class User(UserMixin):
    def __init__(self, id, role):
        self.id = id
        self.role = role

    @property
    def permissions(self):
        return roles_permissions.get(self.role, [])

@login_manager.user_loader
def load_user(user_id):
    user_data = users_db.get(user_id)
    if user_data:
        return User(user_id, user_data["role"])
    return None

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users_db.get(username)

        if user and user["password"] == password:
            login_user(User(username, user["role"]))
            return redirect(url_for("dashboard"))
        else:
            return "Invalid username or password.", 401

    return render_template("login.html")

@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route("/action/<permission>")
@login_required
def action(permission):
    if permission in current_user.permissions:
        return f"Permission '{permission}' granted for {current_user.role} role.", 200
    return f"Permission '{permission}' denied for {current_user.role} role.", 403

if __name__ == "__main__":
    app.run(debug=True)
