from flask import Flask
from csv_op import csv
from SqlParser import SqlParser
app = Flask(__name__)


#obj1 = csv() # create object
parser = SqlParser()
@app.route('/')
def index():
    return "Welcome To SQL Parser"


@app.route('/select')
def select():
      #upload file get its name
      s = csv("student.csv") # create object
      text = "select last_name from student"
      result = parser.unittest_parser(text)
      print(result[0])
      print(s.select(result[0]))
      return "done"
 

if __name__ == '__main__':
    app.run(debug=True)