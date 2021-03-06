import os
from flask import Flask, request, jsonify
from flask_cache import Cache
from api.factMaker import fact_join

app = Flask(__name__)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

default_config = 'config.Development'

app.config.from_object(os.environ.get('WIKI_CONFIG') or default_config)

cache_timeout = app.config['CACHE_TIMEOUT']

@app.route('/<word1>/<word2>')
@app.route('/<word1>', defaults={'word2': None})
@app.route('/', defaults={'word1': None, 'word2': None})
@cache.memoize(cache_timeout)
def index(word1, word2):
    result = fact_join(word1, word2)
    return jsonify(result)
