from flask import Flask, render_template, request, redirect, url_for, flash
from main import Emailer, ZodiacCompatibility, User
import os

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")  # Required for session management


emailer = Emailer()
zodiac_compatibility = ZodiacCompatibility()


@app.route("/")
def index():
    return render_template("index.html", valid_zodiac_signs=User.valid_zodiac_signs)


@app.route("/send", methods=["POST"])
def send_email():
    user_email = request.form.get("email")
    user_zodiac = request.form.get("zodiac")

    user = User(user_email)
    if not user.validate_email():
        flash("Invalid email address.", "error")
        return redirect(url_for("index"))

    if user_zodiac not in User.valid_zodiac_signs:
        flash("Invalid zodiac sign. Please choose a valid sign.", "error")
        return redirect(url_for("index"))

    # Fetch the compatibility data
    compatibility_data = zodiac_compatibility.fetch_compatibility(user_zodiac)
    if not compatibility_data:
        flash("Failed to fetch compatibility data.", "error")
        return redirect(url_for("index"))

    # Format the data
    formatted_data = ZodiacCompatibility.format_compatibility_data(compatibility_data)
    if formatted_data is None:
        flash("Error formatting compatibility data.", "error")
        return redirect(url_for("index"))

    # Send the email
    try:
        subject = f"Your Daily Horoscope and Compatibility for {user_zodiac}"
        emailer.send_email(user_email, subject, formatted_data)
        flash("Email sent successfully!", "success")
    except Exception as e:
        flash(f"An error occurred while sending email: {str(e)}", "error")

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
