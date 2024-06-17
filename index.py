from instaloader import Instaloader, Post


loader = Instaloader()

file = open('./urls.txt', 'r')
urls = file.readlines()

for url in urls:
    video_id = url.split('/')[4]
    post = Post.from_shortcode(loader.context, video_id)
    loader.download_post(post, video_id)
