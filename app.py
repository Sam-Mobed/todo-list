from flask import Flask, render_template, request, redirect, url_for
#Flash is the application itself
#render_template: so that we can work with html files
#request: so that we can access the post request data and data from the HTML file
#redirect: to redirect to different endpoints
#url_for: to get the URLs for the respective end points

app = Flask(__name__, template_folder="templates")

#this will contain our dictionaries
todos = [{"task": "Sample Todo", "done": False}]

#we define a basic endpoint
#route / is simply going to lead to the function index, which renders the index template
@app.route("/")
def index():
    return render_template("index.html", todos=todos)
    #we'll use jinja as a template engine for our index.html file

#we also need different endpoints for adding/editing/removing todos
@app.route("/add", methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({"task": todo, "done": False})
    return redirect(url_for("index"))

@app.route("/edit/<int:index>", methods = ["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form["todo"]
        return redirect(url_for("index"))
    else:
        return render_template("edit.html", todo=todo, index=index)
    
@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for("index"))

@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("index"))

if __name__=='__main__':
    app.run(debug=True)