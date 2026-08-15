from flask import Flask, jsonify, request
from models import UserProfile, db

app = Flask(__name__)

# Creates smart_care.db file automatically inside smart care backend/instance/
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smart_care.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# Home Endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify(
        {"status": "success", "message": "Smart Care Backend is Running!"}
    )


# Save User Health Profile Endpoint
@app.route("/api/user/profile", methods=["POST"])
def create_profile():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("age"):
        return (
            jsonify(
                {"status": "error", "message": "Name and Age are required!"}
            ),
            400,
        )

    new_user = UserProfile(
        name=data.get("name"),
        age=data.get("age"),
        height=data.get("height"),
        weight=data.get("weight"),
        allergies=data.get("allergies"),
        existing_conditions=data.get("existing_conditions"),
        current_medications=data.get("current_medications"),
    )

    db.session.add(new_user)
    db.session.commit()

    return (
        jsonify(
            {
                "status": "success",
                "message": "User profile created successfully!",
                "user": new_user.to_dict(),
            }
        ),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)