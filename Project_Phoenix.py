from flask import Flask
app = Flask(__name__)
votes={}
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

@app.route('/vote/record/<int:choice>')
def vote_record(choice):
    global votes
    if not choice in votes: votes[choice] = 0
    votes[choice]+=1
    return "OK"

@app.route('/vote/debug')
def vote_debug():
    global votes
    answer = "<pre>"
    for i in votes:
        answer = answer + "%d -> %d<br>" % (i, votes[i])
    return answer



if __name__ == '__main__':
    app.run()


