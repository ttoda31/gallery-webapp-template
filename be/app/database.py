from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

_STUB_DATA_DIR = "./stub_data"

_DATABASE_URI = f"sqlite:///{_STUB_DATA_DIR}/stub.db"
engine = create_engine(_DATABASE_URI, connect_args={"check_same_thread": False}, echo=False)
Base = declarative_base()
Base.metadata.reflect(engine)

THUMBNAIL_DIR = _STUB_DATA_DIR + "/thumbs"


class Item(Base):
    __table__ = Base.metadata.tables["items"]

    # uid = Column("uid", String, primary_key=True)
    # title = Column("title", String)
    # description = Column("description", String)
    # date = Column("date", String)
    # url = Column("url", String)
    # categories = Column("categories", String)
    # tags = Column("tags", String)
    # thumbnail_path = Column("thumbnail_path", String)
    # number_of_views = Column("number_of_views", Integer, default=0)


class Category(Base):
    __table__ = Base.metadata.tables["categories"]

    # uid = Column("uid", String, primary_key=True)
    # name = Column("name", String)
    # number_of_items = Column("number_of_items", Integer, default=0)
    # number_of_views = Column("number_of_views", Integer, default=0)
    # number_of_searchs = Column("number_of_searchs", Integer, default=0)


class Tag(Base):
    __table__ = Base.metadata.tables["tags"]

    # uid = Column("uid", String, primary_key=True)
    # name = Column("name", String)
    # number_of_items = Column("number_of_items", Integer, default=0)
    # number_of_views = Column("number_of_views", Integer, default=0)
    # number_of_searchs = Column("number_of_searchs", Integer, default=0)


Base.metadata.create_all(bind=engine)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
