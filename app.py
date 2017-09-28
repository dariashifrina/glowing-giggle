from flask import Flask, render_template, redirect
from util import occupationHelper
import random
app = Flask(__name__)

#Redirects route to occupations route
@app.route("/")
def hello_world():
    return redirect("/occupations")
                                                                           
@app.route("/occupations")
def occupations():
        occupation = occupationHelper.random_occupation()
	#Passes webpage from template, dictionary of Job Class, Percentage, and Link, and link to corresponding random profession
	return render_template( 'occ_page.html', my_dict = occupationHelper.get_dic(), my_occ = occupation, my_link = occupationHelper.occupation_link(occupation))

if __name__ == "__main__":
	app.debug = True
	app.run()
