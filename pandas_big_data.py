import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://crawler:Crawler@1234@10.18.4.211:3367/crawler_web_new?charset=utf8')
def read_sql(table,engine,chunksize=None,return_generator=True):

        if chunksize is not None and chunksize<=0:
            chunksize=None
        result=pd.read_sql(table,engine,chunksize=chunksize)
        if return_generator:
            return result
        else:
            if chunksize is None:
                return result
            else:
                result=list(result)
                if len(result)==0:
                    return pd.DataFrame()
                else:
                    result=pd.concat(result,axis=0)
                    return result 


ret = read_sql('hlj_shixin_1106',engine,chunksize=50,return_generator=False)
print(ret.head(50))