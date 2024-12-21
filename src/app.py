from flask import Flask, render_template, jsonify, request
from databaser import Databaser

app = Flask(__name__)
db = Databaser()

current_video_id = 0

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/videos', methods=['GET', 'POST'])
def video():
    if request.method == 'POST':
        data = request.json
        direction = data.get('direction')

        if direction == 'up':
            video = get_next_video()
            return jsonify(video)

        elif direction == 'down':
            video = get_prev_video()
            return jsonify(video)

    video = db.get_videos()[0]
    return render_template('video.html', video=video)

def get_next_video():
    global current_video_id
    videos = db.get_videos()

    current_video_id = (current_video_id + 1) % len(videos)
    return videos[current_video_id]

def get_prev_video():
    global current_video_id
    videos = db.get_videos()

    current_video_id = (current_video_id - 1) % len(videos)
    return videos[current_video_id]
        
if __name__ == '__main__':
    app.run()
