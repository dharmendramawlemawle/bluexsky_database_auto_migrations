from database import SessionLocal, engine
from routers.user import Hash
import pandas as pd
import random
from faker import Faker
from sqlalchemy.orm import sessionmaker
from models import Base, User, Posts, Comments, Category, PostCategory, Like

# Database configuration

session = SessionLocal()

# Initialize Faker
fake = Faker()

# Generate sample data
def create_sample_data():
    # Users
    users_data = []
    for _ in range(10):
        user = {
            "username": fake.user_name(),
            "email": fake.email(),
            "password": Hash.bcrypt("123456"),
            "status": "Active"
        }
        users_data.append(user)
    users_df = pd.DataFrame(users_data)

    # Posts
    posts_data = []
    for _ in range(30):
        post = {
            "title": fake.sentence(),
            "content": fake.text(),
            "author_id": random.choice(users_df.index) + 1
        }
        posts_data.append(post)
    posts_df = pd.DataFrame(posts_data)

    # Comments
    comments_data = []
    for _ in range(50):
        comment = {
            "content": fake.sentence(),
            "post_id": random.choice(posts_df.index) + 1,
            "author_id": random.choice(users_df.index) + 1
        }
        comments_data.append(comment)
    comments_df = pd.DataFrame(comments_data)

    # Categories
    categories = ["Technology", "Science", "Health", "Business", "Entertainment"]
    categories_df = pd.DataFrame({"name": categories})

    # PostCategories
    post_categories_data = []
    for post_id in posts_df.index + 1:
        for _ in range(random.randint(1, 3)):
            post_category = {
                "post_id": post_id,
                "category_id": random.choice(categories_df.index) + 1
            }
            post_categories_data.append(post_category)
    post_categories_df = pd.DataFrame(post_categories_data)

    # Likes
    likes_data = []
    for post_id in posts_df.index + 1:
        for _ in range(random.randint(0, 5)):
            like = {
                "user_id": random.choice(users_df.index) + 1,
                "post_id": post_id
            }
            likes_data.append(like)
    likes_df = pd.DataFrame(likes_data)

    return users_df, posts_df, comments_df, categories_df, post_categories_df, likes_df

def insert_data(session, df, model):
    for _, row in df.iterrows():
        obj = model(**row.to_dict())
        session.add(obj)
    session.commit()

# Generate sample data
users_df, posts_df, comments_df, categories_df, post_categories_df, likes_df = create_sample_data()

# Insert sample data into the database
users_df.to_sql('users', con=engine, if_exists='append', index=False)
posts_df.to_sql('posts', con=engine, if_exists='append', index=False)
comments_df.to_sql('comments', con=engine, if_exists='append', index=False)
categories_df.to_sql('categories', con=engine, if_exists='append', index=False)
post_categories_df.to_sql('post_categories', con=engine, if_exists='append', index=False)
likes_df.to_sql('likes', con=engine, if_exists='append', index=False)

print("Sample data inserted successfully.")
