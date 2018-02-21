import fresh_tomatoes
import media

#实例化各个对象
TheGodfather = media.Movie("The Godfather",
                           "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BY2Q2NzQ3ZDUtNWU5OC00Yjc0LThlYmEtNWM3NTFmM2JiY2VhXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,700,1000_AL_.jpg",
                           "https://youtu.be/sY1S34973zA")

Avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

AboutTime = media.Movie("About Time",
                        "A very sweet story",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA1ODUzMDA3NzFeQTJeQWpwZ15BbWU3MDgxMTYxNTk@._V1_SY1000_CR0,0,631,1000_AL_.jpg",
                        "https://youtu.be/vwkB3kfnUbk")

#准备电影列表
movies = [TheGodfather, Avatar, AboutTime]

#打开接口
fresh_tomatoes.open_movies_page(movies)
