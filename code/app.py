from flask import Flask, jsonify


app = Flask(__name__)



@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>/<end>
    )


@app.route("/api/v1.0/precipitation")
def precipitation():


    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query all passengers
    results = session.query(Passenger.name).all()

    session.close()
# important because someone will come and run the code again, if too many servers running,
# eventually flask is going to not like that and die

# we have RESULTS now going to convert into a list
    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))
# and then jsonify list
    return jsonify(all_names)
# where the jsonify thing comes in ^^^
# thats done



# now for individual passenger
@app.route("/api/v1.0/stations")
def passengers():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # doing the same query, name, age, sex
    # Query all passengers
    results = session.query(Passenger.name, Passenger.age, Passenger.sex).all()

    session.close()

# creating a dicctionary from those results ^^
    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        #create this dictionary
        passenger_dict = {}
        # create keys and give them a value
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)
# then out put it and this will create a json object
    return jsonify(all_passengers)



@app.route("/api/v1.0/tobs")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)




@app.route("/api/v1.0/<start>/<end>")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)




# and then back to the main
if __name__ == '__main__':
    app.run(debug=True)
