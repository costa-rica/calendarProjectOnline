from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/")
@app.route("/index")
def index():
    return """
    <h2>home</h2><br/>
    This is just to show how we can write html in the python (flask) file
    <br/><br/>
    Here is a link to the <a href="calendar"> calendar</a>
    <!--if you notice the href in the line above doesn't have calendar.html like the html file would-->
    <br/><br/>
    Here's something else that is kinda odd: The link between the calendar page doesn't work when running off
    views.py. However, it does work if we open it straight from the brower. Can you figure out why? Fix?
    """

@app.route("/calendar")
def calendar():
    return render_template("calendar.html")


if __name__ == "__main__":
    app.run(debug=True)