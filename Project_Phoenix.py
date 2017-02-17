from flask import Flask,jsonify
import json
import datetime
app = Flask(__name__)
votes={}
song_count=0
song_data={}

@app.route('/song_data/set/<int:id>/<name>/<album>/<artist>/<int:year>')
def set_song_data(id,name,album,artist,year):
    global song_data
    song_data[int(id)] = {
        'name': name,
        'album': album,
        'artist': artist,
        'year': year,
        'stats': [],
    }
    return "OK"

@app.route('/song_data/get')
def get_song_data():
    global song_data
    return json.dumps(song_data, indent=4)


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

@app.route('/vote/result')
def vote_result():
    global votes
    max_key=-1
    for i in votes:
        if max_key==-1 or votes[i]> votes[max_key]:
            max_key = i
    song_data[max_key]['stats'].append({                    # KALOOOOOOOOOOOOOOOOOOOOOOO
    #    'time': datetime.datetime.now(),                   #removed due to 'time': datetime.datetime.now() error!

        'votes' : votes[max_key],
        'percentage' : votes[max_key]/sum(votes) *100 if sum(votes) > 0 else 0,

    })
    return str(max_key)


if __name__ == '__main__':
    app.run()


