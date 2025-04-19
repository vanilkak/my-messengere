from flask import Flask, send_from_directory, request, jsonify
import os
import time

app = Flask(__name__, static_folder='static')

# Хранилище сообщений
messages = []

# Главная страница
@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# API для работы с сообщениями
@app.route('/api/send', methods=['POST'])
def handle_send():
    data = request.json
    messages.append({
        "user": data.get("user", "Аноним"),
        "text": data.get("text", ""),
        "time": time.strftime("%H:%M:%S")
    })
    return jsonify({"status": "ok"})

@app.route('/api/get', methods=['GET'])
def handle_get():
    return jsonify({"messages": messages})

# Обработчик для статических файлов
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory(app.static_folder, path)

if __name__ == '__main__':
    # Создаём папку static если её нет
    if not os.path.exists(app.static_folder):
        os.makedirs(app.static_folder)
    
    # Запускаем сервер с портом 5000 для всех интерфейсов
    app.run(host='0.0.0.0', port=5000, debug=True)