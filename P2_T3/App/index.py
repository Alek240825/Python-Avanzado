from flask import  Flask, render_template

app=Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/About')
def Acerca_de ():
    return render_template('About.html')

if  __name__ == "__main__":
    app.run(debug = True)

