class sports_news:
    def sports_info(self):
        print("sports news")
        print("sports news")

class political_news:
    def political_info(self):
        print("political news")
        print("political news")
        print("political news")
class movie_news:
    def movie_info(self):
        print("movie news")
        print("movie news")
        print("movie news")

class xyz_news:
    def __init__(self):
        self.sports_news= sports_news()
        self.political_news = political_news()
        self.movie_news = movie_news()

    def total_info(self):
        print("Welcome to xyz news")
        self.movie_news.movie_info()
        self.sports_news.sports_info()
        self.political_news.political_info()

ob = xyz_news()
ob.total_info()