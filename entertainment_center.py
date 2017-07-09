import media
import fresh_tomatoes

# This module contains my favorite movies and makes the movie objects out of
# them.

cars3 = media.Movie("Cars 3",
                    "Lightning McQueen is racing with his long time friends"
                    " Bobby Swift and Cal Weather",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BM" +
                    "Tc0NzU2OTYyN15BMl5BanBnXkFtZTgwMTkwOTg2MTI@._V1_SY1000_" +
                    "CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=2LeOH9AGJQM",
                    3606752)
cars2 = media.Movie("Cars 2",
                    "Star race car Lightning McQueen and his pal Mater head" +
                    " overseas to compete in the World Grand Prix race. But " +
                    "the road to the championship becomes rocky as Mater gets"
                    " caught up in an intriguing adventure of his own:"
                    " international espionage.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMT"
                    "UzNTc3MTU3M15BMl5BanBnXkFtZTcwMzIxNTc3NA@@._V1_SY1000_"
                    "CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=oFTfAdauCOo",
                    1216475)
car1 = media.Movie("Cars",
                   "While traveling to California for the dispute of the"
                   " final race of the Piston Cup against The King and"
                   " Chick Hicks, the famous Lightning McQueen accidentally"
                   " damages the road of the small town Radiator Springs"
                   " and is sentenced to repair it. Lightning McQueen has "
                   "to work hard and finds friendship and love in the " +
                   "simple locals, changing its values during his stay in"
                   " the small town and becoming a true winner. Written by"
                   " Claudio Carvalho, Rio de Janeiro, Brazil",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5B"
                   "MTg5NzY0MzA2MV5BMl5BanBnXkFtZTYwNDc3NTc2._V1_.jpg",
                   "https://www.youtube.com/watch?v=SbXIj2T-_uk",
                   317219)
nemo = media.Movie("Finding Nemo",
                   "After his son is captured in the Great Barrier Reef and" +
                   " taken to Sydney, a timid clownfish sets out on a journey"
                   " to bring him home.",
                   "https://images-na.ssl-images-amazon.com/images/M/MV5BZTA"
                   "zNWZlNmUtZDEzYi00ZjA5LWIwYjEtZGM1NWE1MjE4YWRhXkEyXkFqcGde"
                   "QXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,671,1000_AL_.jpg",
                   "https://www.youtube.com/watch?v=wZdpNglLbt8",
                   266543)
frozen = media.Movie("Frozen",
                     "When the newly crowned Queen Elsa accidentally uses her"
                     " power to turn things into ice to curse her home in" +
                     " infinite winter, her sister, Anna, teams up with a " +
                     "mountain man, his playful reindeer, and a snowman to " +
                     "change the weather condition.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5B" +
                     "MTQ1MjQwMTE5OF5BMl5BanBnXkFtZTgwNjk3MTcyMDE@._V1_SY1" +
                     "000_CR0,0,674,1000_AL_.jpg",
                     "https://www.youtube.com/watch?v=hb8WDATVB6A",
                     229462)
nemo2 = media.Movie("Finding Dory",
                    "The friendly but forgetful blue tang fish, Dory, " +
                    "begins a search for her long-lost parents, and " +
                    "everyone learns a few things about the real meaning" +
                    " of family along the way.",
                    "https://images-na.ssl-images-amazon.com/images/M/" +
                    "MV5BNzg4MjM2NDQ4MV5BMl5BanBnXkFtZTgwMzk3MTgyODE@._" +
                    "V1_SY1000_CR0,0,674,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=UXpe8-zCwhI",
                    227786)

movies = [cars3, cars2, car1, nemo, nemo2, frozen]

# The open movies page method takes in an array of movie objects and produces
# a webpage of movies.
fresh_tomatoes.open_movies_page(movies)
