# Import Dependencies
#################################################
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################



@app.route("/")
def homepage():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/precipitation'> /api/v1.0/precipitation</a><br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/stations'>/api/v1.0/stations<br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/tobs'>/api/v1.0/tobs<br/>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/2016-07-29'>/api/v1.0/&lt;start date &gt;</a> use date format:YYYY-MM-DD <br>"
        f"<a href='http://127.0.0.1:5000/api/v1.0/2016-07-29/2017-07-29'>/api/v1.0/&lt;start date &gt;/&lt;end date&gt;</a>use date format:YYYY-MM-DD"
    )



@app.route("/api/v1.0/precipitation")
def precipitation():

#     # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all precipitations
    results = session.query(measurement.date,measurement.prcp).all()

    session.close()

    # Convert list of tuples into normal list
    all_date_prcp = []
    for date,precip in results:
        date_dict = {}
        date_dict[date] = precip
        all_date_prcp.append(date_dict)

    return jsonify(all_date_prcp)



# now for individual passenger
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

  
    results = session.query(station.station).all()
    print(results)
    session.close()

# creating a dicctionary from those results ^^
    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for stations in results:
        #create this dictionary
        allstations_dict = {}
        # create keys and give them a value
        allstations_dict["stations"] = stations[0]
        
        all_stations.append(allstations_dict)
# then out put it and this will create a json object
    return jsonify(all_stations)



# @app.route("/api/v1.0/tobs")
#query for the dates and temperature observations from a year from the last data point.
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of tobs (temperature observations) for the last year of data in the table"""
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    results = session.query(measurement.tobs).\
        filter(measurement.date >= query_date).all()
        
    session.close()

    # Convert list of tuples into normal list
    all_tobs = list(np.ravel(results))

    return jsonify(all_tobs)


# Create function to validate input as specific date format YYYY-MM-DD
def validate(date_text):
    try:
        dt.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")


# @app.route("/api/v1.0/<start>/<end>")
# def precipitation():

#     # Create our session (link) from Python to the DB
#     session = Session(engine)




# and then back to the main
if __name__ == '__main__':
    app.run(debug=True)
