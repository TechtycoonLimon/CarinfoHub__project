from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# ── Create database and users table ──
def init_db():
    conn = sqlite3.connect("users.db")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            email    TEXT    UNIQUE NOT NULL,
            password TEXT    NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# ── Register ──
@app.route("/register", methods=["POST"])
def register():
    data     = request.get_json()
    email    = data.get("email")
    password = data.get("password")

    try:
        conn = sqlite3.connect("users.db")
        conn.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
        conn.commit()
        conn.close()
        return jsonify({"message": "Registered successfully!"})
    except sqlite3.IntegrityError:
        return jsonify({"message": "Email already registered."}), 400

# ── Login ──
@app.route("/login", methods=["POST"])
def login():
    data     = request.get_json()
    email    = data.get("email")
    password = data.get("password")

    conn = sqlite3.connect("users.db")
    user = conn.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password)).fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login successful!"})
    else:
        return jsonify({"message": "Invalid email or password."}), 401

if __name__ == "__main__":
    init_db()
    print("Server running on http://localhost:5000")
    app.run(debug=True)
