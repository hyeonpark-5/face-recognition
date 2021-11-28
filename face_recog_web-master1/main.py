from flask import Flask, request, flash
from flask import redirect, url_for #redirect
from flask import render_template #template
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/sorkg/Documents/face_recog_web-master/face_images'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
# check file extension

@app.route('/', methods=['GET', 'POST'])
def home():
    # def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        print(request.form)
        idnum = request.form['idnum']
        name = request.form['nm']

        filename = "_".join([idnum, name]) #change filename to "id_name"
        currentfolder=os.mkdir(UPLOAD_FOLDER + "/" + filename )
        filename = "".join([filename, '.', file.filename.rsplit('.', 1)[1]])
        
        file.save(os.path.join([currentfolder,filename]))
    return render_template("index.html")
# {{content}} will be replaced

if __name__ == "__main__":
    HOST=os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT=int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT=5555
    app.run(HOST, PORT, debug=True)
# "debug=True": don't have to rerun the server everytime I make a change
# automatically update the website by detecting changes