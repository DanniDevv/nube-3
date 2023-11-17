#!/usr/bin/env python

from flask import Flask, jsonify
import pandas as pd
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

# Cargar datos desde los archivos CSV
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Realizar alguna manipulación de datos si es necesario

@app.route("/")
def index():
    return "Usage: http://<hostname>[:<prt>]/api/movies"

@app.route("/api/movies")
def get_movies():
    # Check if the data is in the cache
    cached_data = redis.get('movies_data')
    if cached_data:
        # If cached, return cached data
        return jsonify(eval(cached_data))

    # If not in cache, convert the data to JSON
    data = movies.to_dict(orient='records')

    # Store the data in the cache with a timeout of 60 seconds (adjust as needed)
    redis.setex('movies_data', 60, str(data))

    return jsonify(data)

@app.route("/api/ratings")
def get_ratings():
    # Check if the data is in the cache
    cached_data = redis.get('ratings_data')
    if cached_data:
        # If cached, return cached data
        return jsonify(eval(cached_data))

    # If not in cache, convert the data to JSON
    data = ratings.to_dict(orient='records')

    # Store the data in the cache with a timeout of 60 seconds (adjust as needed)
    redis.setex('ratings_data', 60, str(data))

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
