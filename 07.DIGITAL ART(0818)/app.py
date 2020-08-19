
from flask import Flask, render_template, Response, request
from camera import VideoCamera
from style_camera import StyleVideoCamera

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("/home.html")

@app.route('/style')
def style():
    return render_template("/style.html")

@app.route('/style2/<param>', methods=['GET'])
def style2(param) ->str:
    # param = request.form['id']
    print(param)
    return param , " ajax"
##################################################################################
@app.route('/video')
def video():
    return render_template("/video.html")

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')
##################################################################################
@app.route('/style_video')
def style_video():
    return render_template("/style_video.html")

def style_gen(style_camera):
    while True:
        frame = style_camera.get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/style_video_feed')
def style_video_feed():
    return Response(style_gen(StyleVideoCamera()),mimetype='multipart/x-mixed-replace; boundary=frame')
##################################################################################

@app.route('/first')
def first():
    return render_template("/first.html")

@app.route('/faceswap')
def faceswap():
    return render_template("/faceswap.html")

@app.route('/about')
def about():
    return render_template("/about.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
