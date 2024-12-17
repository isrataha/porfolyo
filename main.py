# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

# İçerik sayfasını çalıştırma
@app.route('/')
def index():
    return render_template('index.html')


# Dinamik beceriler
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get("button_html")
    button_db = request.form.get("button_db")
    email = request.form.get("email")
    text = request.form.get("text")
    if email and text:
        with open("a.txt", "a", encoding="utf-8") as f:
            f.write(f"{email}\n")
            f.write(f"{text}\n")
            f.write("------------------------------\n")
    return render_template('index.html', button_python=button_python, button_discord = button_discord, button_html = button_html, button_db = button_db, email = email, text = text)

if __name__ == "__main__":
    app.run(debug=True)
