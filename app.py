from flask import Flask

app = Flask(__name__)



### Please keep this page clean ,, Create classes for ur work then call them here

#Like i did below

from FaceRecognation import DeepLearning # import class
obj1 = DeepLearning() # create object

@app.route('/')
def index():
    return "hello world"

@app.route('/mask')
def mask():
     return obj1.Mask_Detection() # Call the method
 

if __name__ == '__main__':
    app.run(debug=True)

###########################Please Read THiss#################################################################
#After cloning this project
#All python libraries are in requirments.txt 
#so u must create virtual env to install theses libires from requirments.txt
## so watch this video https://www.youtube.com/watch?v=mBcmdcmZXJg


#Watch This
#https://www.youtube.com/watch?v=2QP4QxzG-wY
#https://www.youtube.com/watch?v=5co5C3jmTWI
####
## After watching 
## TO push to Master 

## git add . 
## git commit -m "Write ur message here explaing what u did"
## git push origin main

### U will notice File .gitignore  it ignores pushing python virtual environmet so it dosen't push python libraries


