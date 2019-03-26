from sqlalchemy import create_engine as __ce__
from datetime import datetime as __dt__
import pandas as __pd__

class engine():
    __engine__ = None

    def __init__(self, host='localhost', database='postgres', user='postgres', password='postgres'):
        self.__engine__ = "postgresql://" + user + ":" + password + "@" + host + "/" + database

    def dump(self, schema, table, df):
        try:
            engine = __ce__(self.__engine__)
            if engine.dialect.has_table(engine, table, schema = schema):
                backup = table + '_' + __dt__.strftime(__dt__.now(), '%d%m%y_%H%M%S')
                __pd__.read_sql_query("select * from {}.{};".format(schema, table), engine).to_sql(backup, con=engine, if_exists='replace', schema=schema, index=False)
                print(backup + ' table Created Successfully')

            df.to_sql(table, con=engine, if_exists='replace', schema=schema, index=False)
            print(table + ' table Dumped Successfully')
        except Exception as e:
            print(e)
        finally:
            engine.dispose()

    def read_table(self, schema, table):
        try:
            engine = __ce__(self.__engine__)
            return __pd__.read_sql_query("select * from {}.{};".format(schema, table), engine)        
        except Exception as e:
            print(e)
        finally:
            engine.dispose()