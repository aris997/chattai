from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    make_response,
    redirect,
    # url_for,
)
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from flask_bcrypt import Bcrypt
from datetime import timedelta


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret-key-goes-here"
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)  # Token expires in 1 hour
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


# Simulated user database
users = {"admin": bcrypt.generate_password_hash("password1").decode("utf-8")}


@app.route("/")
def home():
    return render_template("index.html")


@jwt.unauthorized_loader
def custom_unauthorized_response(_err):
    return render_template("404.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return redirect("/")

    data: dict = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if username in users and bcrypt.check_password_hash(users.get(username), password):
        access_token = create_access_token(identity=username)
        resp = make_response(jsonify({"login": True}), 200)
        resp.set_cookie("access_token_cookie", access_token)
        return resp

    return jsonify({"msg": "Invalid credentials"}), 401


@app.route("/logout", methods=["POST"])
def logout():
    resp = make_response(jsonify({"logout": True}), 200)
    resp.delete_cookie("access_token_cookie")
    return resp


@app.route("/dashboard", methods=["GET"])
@jwt_required()
def dashboard():
    current_user = get_jwt_identity()
    print(current_user)
    return render_template("dashboard.html", user=current_user)


if __name__ == "__main__":
    app.run(debug=True)
