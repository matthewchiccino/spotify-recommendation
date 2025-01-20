from flask import Flask, request, jsonify, render_template, session
from flask_session import Session
from flask_cors import CORS
from functionality import get_artist

app = Flask(__name__)
CORS(app)

# Configure Flask-Session
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in files (use Redis for production)
app.config['SECRET_KEY'] = 'your_secret_key'
Session(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/info.html')
def info():
    return render_template('info.html')

@app.route('/help.html')
def help():
    return render_template('help.html')


@app.route('/submit', methods=['POST'])
def guess_word():
    data = request.get_json()
    print(data)
    artist = get_artist(data)
    
    return jsonify({
        "message": artist,
    })


# for local testing
if __name__ == '__main__':
    app.run(debug=True, port=8080)