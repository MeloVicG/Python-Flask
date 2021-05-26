from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='color:red'>hello Im Here</h1>"

@app.route('/blue')
def blue():
    return "<h1 style='color:blue'>hello Im Here!</h1>"

                    #can be <int:num>
@app.route('/<color>/<num>')
def color(color, num):
    print(color, num)
    html_str = ""

    for i in range(int(num)):
        html_str += f"<h1 style='color:{color}'>hello Im Here!</h1>"
    return html_str

if __name__ == "__main__":
    app.run(debug=True)