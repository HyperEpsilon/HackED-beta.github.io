from flask import Flask, send_file, render_template
from flask_socketio import SocketIO, emit
import mapGen


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@socketio.on('mapUpdateEvent')
def map():
    mapGen.createHeatMap()
    print("I ran bitches")

    return send_file('heatMap.html', mimetype='text/html')

@app.route('/sms', methods=['GET','POST'])
def index():
    return render_template("index.html")
if __name__ == "__main__":
    socketio.run(app)
    #app.run(debug = True)