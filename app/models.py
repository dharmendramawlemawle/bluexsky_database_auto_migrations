from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True, index=True) 
    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    status = Column(String(45), nullable=False, default="ACTIVE")
    
    post = relationship("Posts", back_populates="author")
    comment = relationship("Comments", back_populates="author")
    liked_post = relationship("Like", back_populates="user")
    

class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    content = Column(String(255))
    author_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates ="post")
    comment = relationship("Comments", back_populates="post")
    category = relationship("PostCategory", back_populates="post")
    like = relationship("Like", back_populates="post")


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255))
    post_id= Column(Integer, ForeignKey("posts.id"))
    author_id = Column(Integer, ForeignKey("users.id"))
    
    post = relationship("Posts", back_populates="comment")
    author = relationship("User", back_populates="comment")



class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    
    post = relationship("PostCategory", back_populates="category")



class PostCategory(Base):
    __tablename__ = 'post_categories'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("categories.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    
    post = relationship("Posts", back_populates="category")
    category = relationship("Category", back_populates="post")
    
    

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))

    user = relationship("User", back_populates="liked_post")
    post = relationship("Posts", back_populates="like")
