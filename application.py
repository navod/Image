from flask import Flask,request,Response
from flask.templating import render_template
import os

UPLOAD_FOLDER = './upload'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/upload_image",methods=["GET","POST"])
def upload_image():
    try:
        print(request.method)
        if request.method =='POST':
        
            file = request.files['profile_pic']
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            return path
    
        return render_template("upload_image_form.html")
    except Exception as ex:
        print(ex)
if __name__ == "__main__":
    app.run(debug=True)