class Article:
    def __init__(self,title, content,author):
        self. title = title
        self. content = content
        self. author = author
        self.new_author = None
        self.new_content = None
        self.new_title = None


    def edit(self, new_content):
        self. content = new_content
        return new_content

    def change_author(self, new_author):
        self. author = new_author
        return new_author
    def rename(self, new_title):
        self. title = new_title
        return new_title

    def __repr__(self):
        return f"{self.title} - {self.content}: {self.author}"


article = Article("some title", "some content", "some author")
article.edit("new content")
article.rename("new title")
article.change_author("new author")
print(article)
