#!/usr/bin/env python3
"""
My first Flask app
"""
# Importera relevanta moduler
from flask import Flask, render_template
from flask import request
import person
import data
from farm import Farm

# Create a database connection to our farm and a session.
my_farm = Farm("db/farm.sqlite")

links = list()
links.append(("/", "main", "Me-sida"))
links.append(("/about/", "about", "Om mig"))
links.append(("/redovisning/", "redovisning", "Redovisning"))
links.append(("/farm/animals", "farmAnimals", "Farm"))

my_person = person.Person("Emil", "Mattsson", 24, "Katrineholm")


app = Flask(__name__)


@app.route("/")
def main():
    """ Main route """
    my_data = data.Data(links, links[0][2], "https://avatars1.githubusercontent.com/u/12786962?v=3&s=200")
    return render_template("index.html", data=my_data, person=my_person)



@app.route("/about/")
def about():
    """ About route """
    my_data = data.Data(links, links[1][2], "https://avatars1.githubusercontent.com/u/12786962?v=3&s=200")
    return render_template("about.html", data=my_data, person=my_person)



@app.route("/redovisning/")
def redovisning():
    """ Redovisning route """
    my_data = data.Data(links, links[2][2], "https://avatars1.githubusercontent.com/u/12786962?v=3&s=200")
    return render_template("redovisning.html", data=my_data, person=my_person)



@app.route("/farm/animals/", methods=["POST", "GET"])
def farmAnimals():
    """ Animals route """
    if request.method == "GET":
        int_animalId = request.args.get("del")
        my_farm.deleteAnimal(int_animalId)

    if request.method == "POST":
        my_farm.createAnimal(request.form["Species"], request.form["Name"], int(request.form["Number of legs"]))

    my_data = data.Data(links, links[3][2], "https://avatars1.githubusercontent.com/u/12786962?v=3&s=200")

    return render_template("farm.html", data=my_data, person=my_person, farm=my_farm.displayAnimals())



@app.route("/farm/humans/", methods=["POST", "GET"])
def farmHumans():
    """ Humans route """
    if request.method == "GET":
        int_humanId = request.args.get("del")
        my_farm.deleteHuman(int_humanId)

    if request.method == "POST":
        my_farm.createHuman(request.form["Name"], request.form["Occupation"], int(request.form["Age"]))

    my_data = data.Data(links, links[3][2], "https://avatars1.githubusercontent.com/u/12786962?v=3&s=200")

    return render_template("farm.html", data=my_data, person=my_person, farm=my_farm.displayHumans())



@app.route("/farm/vehicles/", methods=["POST", "GET"])
def farmVehicles():
    """ Vehicles route """
    if request.method == "GET":
        int_vehicleId = request.args.get("del")
        my_farm.deleteVehicle(int_vehicleId)

    if request.method == "POST":
        my_farm.createVehicle(request.form["Type of vehicle"], float(request.form["Price"]))

    my_data = data.Data(links, links[3][2], "https://avatars1.githubusercontent.com/u/12786962?v=3&s=200")

    return render_template("farm.html", data=my_data, person=my_person, farm=my_farm.displayVehicles())



if __name__ == "__main__":
    app.run()
