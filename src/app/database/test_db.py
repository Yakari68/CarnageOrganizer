import sqlalchemy as sa

engine = sa.create_engine("sqlite+pysqlite:///test_db.db")