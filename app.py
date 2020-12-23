from csv_op import csvv
from SqlParser import SqlParser
from flask import Flask, render_template, request, redirect
import os 
from werkzeug.utils import secure_filename
import pandas as pd
from flask import Flask
from flask import render_template
from flask import request
import csv
import uuid
import string
import random

app = Flask(__name__)
#obj1 = csv() # create object
parser = SqlParser()
@app.route('/')
def index():
    return "Welcome To SQL Parser"


ALLOWED_EXTENSIONS = {'csv'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


@app.route('/uploader', methods = ['POST','GET'])
def uploader():

        if request.method == 'GET':
       
         return render_template('app.html') 
        if request.method == 'POST' and "query" not in request.form: 
            f = request.files['file']
            if f and allowed_file(f.filename):

              #  f.save(secure_filename(f.filename))
                id = id_generator()
                f.save(os.path.join('CSVFiles',id+'.csv'))

                results = []
                reader = csv.DictReader(open('CSVFiles/'+id+'.csv'))
                for row in reader:
                    results.append(dict(row))
                #print(results)
                fieldnames = [key for key in results[0].keys()]
                
                return render_template('app.html', results=results, fieldnames=fieldnames, len=len,id=id)
                
            else:
             return "not suppored"
        
        if request.method == "POST" and "query" in request.form:

                #print(request.form['fileID'])
                # s=csv("student.csv")  
              
                fileName=request.form['fileID']
                if not fileName:
                    fileName=request.form['fileIDD']

                csvFile = 'CSVFiles/'+fileName+'.csv'
                s = csvv(csvFile) # create object
                text = request.form['query']
                result = parser.unittest_parser(text)
               # print(result[0])
                try:
                    resultQuery = s.select(result[0])
                    code = s.generateCode(result[0])
                except:
                     return render_template('error.html')
               # print(resultQuery)
                results = []
                
                resultQuery.to_csv('queryy.csv', encoding='utf-8', index=False)
                
                reader = csv.DictReader(open('queryy.csv'))
                for row in reader:
                     results.append(dict(row))
                #print(results)
                fieldnames = [key for key in results[0].keys()]

                return render_template('app.html', results=results, fieldnames=fieldnames, len=len,code=code,fileName=fileName)
                #return "done"
                
            
   
if __name__ == '__main__':
    app.run(debug=True)


