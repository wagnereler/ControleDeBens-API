from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

class Database:
    def __init__(self, database_url):
        self.engine = create_engine(database_url)
        self.metadata = MetaData()
        self.Base = automap_base(metadata=self.metadata)
        self.session = Session(self.engine)

    def reflect_database(self):
        self.metadata.reflect(bind=self.engine)

    def prepare_models(self):
        self.Base.prepare()

    def get_model_class(self, table_name):
        return getattr(self.Base.classes, table_name, None)
