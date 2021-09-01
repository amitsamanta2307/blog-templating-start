import requests


class Post:

    def get_posts(self):
        posts_url = 'https://jsonplaceholder.typicode.com/posts'
        response = requests.get(url=posts_url)
        blogs = response.json()
        return blogs

    def get_post(self, blog_id):
        posts_url = f"https://jsonplaceholder.typicode.com/posts/{blog_id}"
        response = requests.get(url=posts_url)
        blog = response.json()
        return blog
