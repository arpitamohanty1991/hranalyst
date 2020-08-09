import os
from flask import Flask, request, redirect, url_for, make_response, flash, current_app,render_template
from werkzeug.utils import secure_filename
import match_score_calculator
import pandas as pd
import re

UPLOAD_FOLDER = 'C:/Users/Arpita/Desktop/resume/hranalyticszenaura/static/files'
ALLOWED_EXTENSIONS = set(['xls', 'xlsx', 'csv'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# application home page route
@app.route('/')
def index():
    return render_template("index.html")



@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        pastExp = request.form['past_exp']
        corpus = request.form['job_posting_keywords']
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser may
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
#            csv_output = candidate_match_score.processData(filepath, pastExp, corpus)
#            response = make_response(csv_output)
#            response.headers["Content-Disposition"] = "attachment; filename=output.csv"
#            return response
        # after upload if you want to put a message on screen you can pass or you can render it to different html page after processing
    return render_template("index.html")

#@app.route('/Upload-Resume/<path:filename>')
#def custom_static(filename):
#    return send_from_directory('./Upload-Resume', filename)
    
@app.route('/static/<path:filename>')
def send_static(filename):
    return current_app.send_static_file(filename)



if __name__ == "__main__":
    app.run(debug=True)
