from flask import (Flask,jsonify,abort)

app = Flask(__name__)

movies = [
    {
        'id':1,
        'title': 'Money Heist: The Phenomenon',
        'description': 'Money Heist: The Phenomenon is a 2020 behind-the-scenes documentary film directed by Luis Alfaro and Pablo Lejarreta, and written by Pablo Lejarreta and Javier Gómez Santander. It takes a look at the global success of the TV series Money Heist, and features interviews with the creators and cast of the show.'       },
    {
        'id':2,
        'title': 'The Amazing Spider-Man 2',
        'description': 'Spider-Man embarks on a mission to protect his loved ones when OsCorp, owned by his childhood friend Harry Osborn, unleashes a slew of genetically-modified villains against him.'      
    },
    {
        'id':3,
        'title': 'Now You See Me 2',
        'description':'After fleeing from a stage show, the illusionists (Jesse Eisenberg, Woody Harrelson) known as the Four Horsemen find themselves in more trouble in Macau, China. Devious tech wizard Walter Mabry (Daniel Radcliffe) forces the infamous magicians to steal a powerful chip'
    }
    ]
@app.route('/movies',methods=['GET'])
def movies():
    return jsonify({'movies':movies})

@app.route('/movies/<int:movie_id>', methods=['GET'])
def get_movie(movie_id):
    movie = [movie for movie in movies if movie['id'] == movie_id]
    if len(movie) == 0:
        abort(404)
    return jsonify({'movie': movie[0]})

if __name__ == '__main__':
    app.run(debug=True)
