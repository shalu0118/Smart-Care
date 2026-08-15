from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class UserProfile(db.Model):
    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Float, nullable=True)  # in cm
    weight = db.Column(db.Float, nullable=True)  # in kg
    allergies = db.Column(
        db.Text, nullable=True
    )  # e.g., "Penicillin, Peanuts"
    existing_conditions = db.Column(
        db.Text, nullable=True
    )  # e.g., "Diabetes, Hypertension"
    current_medications = db.Column(
        db.Text, nullable=True
    )  # e.g., "Metformin, Paracetamol"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "height": self.height,
            "weight": self.weight,
            "allergies": self.allergies,
            "existing_conditions": self.existing_conditions,
            "current_medications": self.current_medications,
        }