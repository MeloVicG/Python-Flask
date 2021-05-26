
from flask import Flask, render_template  
app = Flask(__name__)   

@app.route('/')         
def index():
    return render_template('index.html', phrase='Hello', times=5)
    
@app.route('/success')
def sucess():
    return "<h1>success<h1>"

@app.route('/<name>/<times>')
def hello(name, times):        
    return render_template('index.html', some_name=name, num_times = int(times))
    
if __name__=="__main__":   
    app.run(debug=True)    
