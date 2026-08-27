from flask import Flask, render_template, request, redirect
import sqlite3
import string
import random
from urllib.parse import urlparse

app = Flask(__name__)

# Database create
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# Generate unique short code
def generate_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choice(characters) for _ in range(length))

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT short_code FROM urls WHERE short_code = ?",
            (code,)
        )

        result = cursor.fetchone()
        conn.close()

        if result is None:
            return code


# Check valid URL
def is_valid_url(url):
    try:
        result = urlparse(url)

        return result.scheme in ["http", "https"] and result.netloc != ""

    except:
        return False


# Home page
@app.route("/", methods=["GET", "POST"])
def home():

    short_url = None
    error = None

    if request.method == "POST":

        original_url = request.form.get("url", "").strip()

        # Empty URL
        if not original_url:
            error = "Please enter a URL."

        # Invalid URL
        elif not is_valid_url(original_url):
            error = "Please enter a valid URL."

        else:
            short_code = generate_code()

            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO urls (original_url, short_code) VALUES (?, ?)",
                (original_url, short_code)
            )

            conn.commit()
            conn.close()

            short_url = request.host_url + short_code

    return render_template(
        "index.html",
        short_url=short_url,
        error=error
    )


# Redirect short URL
@app.route("/<short_code>")
def redirect_url(short_code):

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code = ?",
        (short_code,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return redirect(result[0])

    return "Short URL not found!", 404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)