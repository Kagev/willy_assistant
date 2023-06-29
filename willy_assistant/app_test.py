from flask import Flask, render_template, request
import pathlib
from willy_assistant.methods.authorization import AuthorizationAdmin, AuthorizationUser
from willy_assistant.methods.registration import RegistrationUser, RegistrationAdmin


app = Flask(
    __name__,
    template_folder="../willy_assistant/templates",
    static_url_path="/static",
    static_folder="../willy_assistant/static",
)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        button_clicked = request.form.get("button_clicked")

        if button_clicked == "signin-btn":
            return render_template("signin.html")
        elif button_clicked == "register-btn":
            return render_template("registration.html")

    return render_template("index.html")


@app.route("/signin", methods=["POST"])
def signin():
    identifier = request.form.get("identifier")
    password = request.form.get("password")

    admin_authorization = AuthorizationAdmin()
    admin_authorization.load_users()

    user_authorization = AuthorizationUser()
    user_authorization.load_users()

    if admin_authorization.login(identifier, password):
        return render_template("dashboard.html")
    elif user_authorization.login(identifier, password):
        return render_template("dashboard.html")
    else:
        return render_template(
            "signin.html",
            error_message="Invalid credentials",
        )


@app.route("/registration", methods=["POST"])
def registration():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    number_phone = request.form.get("phone number")

    user_registration = RegistrationUser()
    user_registration.registration_user(username, password, email, number_phone)

    return "Registration successful"

    return render_template("signin.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
