import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title=movie_title                      #电影名称变量
        self.storyline=movie_storyline              #电影剧情简介变量
        self.poster_image_url=poster_image          #电影海报图片链接变量
        self.trailer_youtube_url=trailer_youtube    #电影预告片链接变量

    # def show_trailer(self):
    #     webbrowser.open(self.trailer_youtube_url)
