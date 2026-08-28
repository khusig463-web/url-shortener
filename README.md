# url-shortener

A simple and user-friendly **URL Shortener Web Application** built using **Python, Flask, SQLite, HTML, CSS, and JavaScript**.

The application converts a long URL into a short, easy-to-share URL. When the generated short URL is accessed, the user is automatically redirected to the original URL.

---

## ✨ Features

- Enter a valid long URL.
- Generate a unique 6-character short code.
- Generate a short URL for the given link.
- Redirect users to the original URL using the short URL.
- Handle empty URL inputs.
- Validate URLs and handle invalid URL inputs.
- Display the generated short URL clearly.
- Copy the generated short URL using the **Copy** button.
- Store URL mappings in an SQLite database.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python** | Backend logic, URL validation, and short-code generation |
| **Flask** | Web framework and routing |
| **SQLite** | Stores original URLs and short codes |
| **HTML** | Creates the web page structure |
| **CSS** | Designs and styles the user interface |
| **JavaScript** | Provides copy-to-clipboard functionality |

---

## 💡 Approach

The application follows a simple URL shortening process:

1. The user enters a long URL.
2. The application validates the URL.
3. Python generates a unique 6-character short code.
4. The original URL and short code are stored in the SQLite database.
5. A short URL is generated and displayed to the user.
6. When the short URL is accessed, Flask searches for the corresponding short code in the database.
7. If the code exists, the user is redirected to the original URL.
8. If the URL is empty or invalid, an appropriate error message is displayed.

---

## 🔄 How It Works

```text
User enters long URL
        ↓
    URL Validation
        ↓
Generate Unique Short Code
        ↓
Store URL + Code in SQLite
        ↓
Display Short URL
        ↓
User opens Short URL
        ↓
Search Code in Database
        ↓
Redirect to Original URL
