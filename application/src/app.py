from flask import Flask

app = Flask(__name__)

# 🎯 Customize this greeting text
greeting_text = "Hello from your DevOps Flask App! This is my project app code hehe!"

@app.route("/")
def home():
    return f"<h1>{greeting_text}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

