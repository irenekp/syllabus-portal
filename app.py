from flask import Flask
from flask_pymongo import PyMongo
from flask import render_template, request
#from werkzeug import secure_filename
import database
import os

#useruploading, serveruploader, filelist, viewfile
app = Flask(__name__)

@app.route("/")
def default():
	return "Go to /test to add something to the database!"

#ToDo: uploadfile.html - prettier, expand the form
@app.route('/useruploading')
def useruploading():
	return render_template('uploadfile.html')

#upload all the new data to atlas.
@app.route('/serveruploader', methods = ['GET', 'POST'])
def serveruploader():
	if request.method == 'POST':
		f = request.files['myfile']
		f.save(os.path.join("static/",f.filename))
		database.db.Resources.insert_one({"course_code":"ABC","filepath":f.filename})
		#f.save(f.filename)
		return 'file uploaded successfully'

#ToDo: filelist: multiple file+properties to template
@app.route('/filelist')
def filelist():
	cursor=database.db.Resources.find( { "course_code": "ABC" } )
	op=""
	for item in cursor:
		print(item)
	return "check commandline"

#display individual file, make it prettier, call it from onclick of 
@app.route("/viewfile")
def viewfile():
	#read filepath from db into filepath variable
	filepath='Entry1.pdf'
	return render_template("showfile.html",filepath=filepath)
"""
@app.route("/test")
def test():
	#read uploaded file>save in static>pass the name here
	filepath="Entry1.pdf"
	database.db.Resources.insert_one({"filepath":filepath})
	return "Connected to the data base!"
"""

if __name__ == '__main__':
	app.run(port=8000)


