def load_movie_list():
    movies = []
    with open('movie_ids.txt', 'r', encoding = "ISO-8859-1") as f:
        for line in f.readlines():
            movie = ' '.join(line.split(' ')[1:])
            movies.append(movie)

    return movies

if __name__ == '__main__':
    movies = load_movie_list()
    print(movies[0])
