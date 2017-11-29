from flask import Flask, jsonify, render_template, url_for

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3020)