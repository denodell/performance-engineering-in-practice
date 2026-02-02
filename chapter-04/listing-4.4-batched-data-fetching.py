posts = await fetch_posts()
author_ids = [post.author_id for post in posts]
authors = await fetch_users(author_ids)
for post in posts:
    post.author = authors[post.author_id]
