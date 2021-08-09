import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    'mysql+pymysql://root:@localhost/visa_HB1_certified', echo=False)


def loadDB():
    data = pd.read_csv("visa_H1B_certified.csv")
    data.to_sql("certified", con=engine)

    rows = data.shape[0]
    return rows


if __name__ == "__main__":
    loadDB()
