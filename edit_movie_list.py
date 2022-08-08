import csv

def getMovieList(file_name):
	with open(file_name, 'r') as f:
		movies = f.readlines()
		movies_list = []
		for col in movies:
			l = col.strip('\n').split(';')
			movies_list.append(l[:-1:])
		return movies_list[3::]

def writeMovieList(new_movie_list, newfile_name):
	with open(newfile_name, 'w') as f:
		w = csv.writer(f)
		w.writerows(new_movie_list)
		return 0

def getYear(date, year):
	if len(date) >= 4 and date[:4].isnumeric():
		movie_year = int(date[:4])
		return True if movie_year >= year else False
	return True

def getMoviesAfterDate(movie_list, year):
	new_movie_list = []
	for movie in movie_list:
		if getYear(movie[1], year):
			new_movie_list.append(movie)
	return new_movie_list
	


def main(file_name, year, newfile_name):
	movie_list = getMoviesAfterDate(getMovieList(file_name), year)
	print(movie_list)
	writeMovieList(movie_list, newfile_name)
	return 0
	

file_name = 'vampire_movies.csv'
newfile_name = 'new_vampire_movies.csv'
year = 1980
main(file_name, year, newfile_name)
