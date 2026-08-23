from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models import UserProfile, db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smart_care.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "success", "message": "Smart Care Backend is Running!"})


@app.route("/api/user/profile", methods=["POST"])
def create_profile():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("age"):
        return jsonify({"status": "error", "message": "Name and Age are required!"}), 400

    if not data.get("email") or not data.get("password"):
        return jsonify({"status": "error", "message": "Email and password are required!"}), 400

    new_user = UserProfile(
        name=data.get("name"),
        email=data.get("email"),
        password_hash=generate_password_hash(data.get("password")),
        age=data.get("age"),
        height=data.get("height"),
        weight=data.get("weight"),
        allergies=data.get("allergies"),
        existing_conditions=data.get("existing_conditions"),
        current_medications=data.get("current_medications"),
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User profile created successfully!",
        "user": new_user.to_dict(),
    }), 201


@app.route("/api/user/profile/<int:user_id>", methods=["GET"])
def get_profile(user_id):
    user = UserProfile.query.get(user_id)
    if not user:
        return jsonify({"status": "error", "message": "User not found"}), 404
    return jsonify({"status": "success", "user": user.to_dict()}), 200


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    user = UserProfile.query.filter_by(email=data.get("email")).first()
    if user and check_password_hash(user.password_hash, data.get("password", "")):
        return jsonify({"status": "success", "user": user.to_dict()}), 200
    return jsonify({"status": "error", "message": "Invalid email or password"}), 401


if __name__ == "__main__":
    app.run(debug=True, port=5000)