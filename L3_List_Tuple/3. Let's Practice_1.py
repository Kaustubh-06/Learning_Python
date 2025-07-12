# WAP to ask the user to enter names of their 3 favourite movies amd store thenm in a list.

fav_movie1 = input("Entrer your fiest movie: ")
fav_movie2 = input("Enter your second movie: ")
fav_movie3 = input("Enter your third movie: ")
Fav_movies = [fav_movie1, fav_movie2, fav_movie3]
print(Fav_movies)  # Output: List of favourite movies

#2nd method
fav_movies = []
fav_movies.append(input("Enter your first movie: "))
fav_movies.append(input("Enter your second movie: "))
fav_movies.append(input("Enter your third movie: "))
print(fav_movies)  # Output: List of favourite movies