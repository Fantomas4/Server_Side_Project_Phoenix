from flask import Flask
app = Flask(__name__)

song_count=0

@app.route('/song_count/get')
def get_song_count():
    global song_count
    return (str(song_count))


@app.route('/song_count/set/<int:count>')
def set_song_count(count):
    global song_count
    song_count=count
    return "OK"




if __name__ == '__main__':
    app.run()


