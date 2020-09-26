import sql as s

from flask import Flask, render_template, request
app = Flask(__name__,template_folder="template")

@app.route("/")
def hello():
    name = "hello"
    return render_template("testIndex.html",name=name)


@app.route("/", methods=['POST'])
def processQuery():
    question = request.form['message']
    data = s.getAnswer(question)
    return render_template("testIndex.html",result=data)

app.run()
