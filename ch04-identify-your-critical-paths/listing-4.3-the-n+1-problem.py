posts = await fetch_posts()
for post in posts:
    post.author = await fetch_user(post.author_id)
