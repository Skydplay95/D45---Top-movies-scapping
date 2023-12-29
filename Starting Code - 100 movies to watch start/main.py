import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

#get the web response 
response = requests.get(url=URL)
#check for error
response.raise_for_status()

#save html page in var
content = response.text

#create soup object to manipulate html content 
soup = BeautifulSoup(content, "html.parser")

#get each html markup who have a movie name 
movies_list = soup.find_all(name="h3", class_="title")

#create a list with only the text of the movies list
movies_name = [movie_name.getText() for movie_name in movies_list]

with open(file="./Starting Code - 100 movies to watch start/movies.txt", mode="a") as file:
  #iterate in the reversed order to go from 1 to 100
  for name in reversed(movies_name):
    #write the name on the movies in the movies file
    file.write(f"{name}\n")
  