

class Author():
    name: str
    age: int

    def __init__(self, n, a):
        self.name = n
        self.age = a

class Article():
    title: str
    description: str
    src: str
    publishingyear: str
    author: Author
    rating: list

    def __init__(self, t, d, s, p):
        self.title = t
        self.description = d
        self.src = s
        self.publishingyear = p
        self.rating = [0,0,0,0,0]
    
    def __str__(self):
        pass #void

    def rate(self, stars):
        if (stars < 1) or (stars > 5): return
        stars -= 1
        self.rating[stars] += 1
    
auth = Author('Dr Manhattan', 200)

post = Article(
    "Dr Manhattan and recursive backtracking",
    "No page order",
    "https://drmanhattanonmanhattan.com/static/post/123454532",
    "2020"
)
post.rate(5)

