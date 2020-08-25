from flask import Flask, render_template, Response, request, jsonify, send_from_directory
from camera import VideoCamera
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("/index.html")



@app.route('/style')
def style():
    return render_template("/generic.html")

@app.route('/style1', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['upload-file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.getcwd()+"/my_photographs1/", "1.jpg"))
            tasks = []

            return jsonify({'tasks': tasks})

@app.route('/style2/<param>', methods=['GET'])
def style2(param) ->str:
    # param = request.form['id']
    print(param)
    # if __name__ == '__main__':
    #     os.system("python main.py --model_name=model_"+param+ " --phase=inference --image_size=1280 --ii_dir ./my_photographs1/ --save_dir=./save_processed_images_here/")
    os.system("python main.py --model_name=model_"+param+ " --phase=inference --image_size=1280 --ii_dir ./my_photographs1/ --save_dir=./save_processed_images_here/")
    return param , " ajax"

@app.route('/file/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    return send_from_directory(directory='save_processed_images_here', filename=filename)

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

@app.route('/firstordervideo')
def first():
    return render_template("/generic1.html")

####################################################################################
@app.route('/faceswap')
def faceswap():
    return render_template("/generic0.html")
####################################################################################

@app.route('/faceswap_video')
def faceswap_video():
    return render_template("/faceswap_video.html")

#######################################################################################
@app.route('/about')
def about():
    return render_template("/about.html")

from flask import send_from_directory


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
