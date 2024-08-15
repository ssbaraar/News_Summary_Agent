from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from utils.config import DATABASE_URL

Base = declarative_base()

# Define your database URL in your config file
from utils.config import DATABASE_URL

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    url = Column(String(255), unique=True, nullable=False)
    source = Column(String(100), nullable=False)
    published_date = Column(DateTime, nullable=False)
    content = Column(Text)
    summary = Column(Text)
    keywords = Column(String(255))
    processed = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Article(id={self.id}, title='{self.title}', source='{self.source}')>"

engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)