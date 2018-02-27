from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/event', methods=['POST'])
def event_received():
    message = request.json['message']
    # do something...
    return jsonify({'status': 'OK'})


if __name__ == '__main__':
    app.run()