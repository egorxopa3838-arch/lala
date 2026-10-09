from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head><title>МУР-техника</title></head>
    <body style="background:#111;color:#0f0;font-family:monospace;text-align:center">
        <h1>🐱 МУР-техника</h1>
        <h2>MeowOS 4.5</h2>
        <p>Процессор: МУР 9999 PRO MAX ULTRA</p>
        <p>Филя: 🐱 на связи</p>
        <hr>
        <a href="/filya" style="color:#0f0">Статус Фили</a><br>
        <a href="/car" style="color:#0f0">Филя Car</a>
    </body>
    </html>
    """

@app.route("/filya")
def filya():
    return "<h1>🐱 Филя</h1><p>Настроение: 🔵 спокойный</p><p>Миска: полная</p>"

@app.route("/car")
def car():
    return "<h1>🚗 Филя Car</h1><p>Мур-мини — 100 000</p><p>Мур-Sport — 1 200 000</p>"

if __name__ == "__main__":
    print("🌐 Сайт запущен!")
    print("📱 Открой в браузере: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)()