from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect("/occupations")

@app.route("/occupations")
def occupations():
	return render_template( 'Template.html', foo="fooooo", collection=coll)

if __name__ == "__main__":
	app.debug = True
	app.run()
