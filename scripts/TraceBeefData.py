from pandas.io.json import json_normalize
from urllib.request import urlopen
import pandas as pd
import json

def getData(date):
    yy = date[0:4] 
    mm = date[5:7]
    dd = date[8:10]
    print(yy, mm, dd)
    target_url = "http://data.coa.gov.tw/Service/OpenData/TraceBeefData.aspx?$skip=0&$filter=SlaughterDate+like+{}%2f{}%2f{}".format(yy,mm,dd)
    res = urlopen(target_url)
    con = res.read().decode(res.headers.get_content_charset())
    raw = json.loads(con)
    df = json_normalize(raw)
    return df

def main():
    start = "2014-01-01"
    end = "2018-10-16"
    date_range = pd.date_range(start, end).tolist()
    date_range = [i.strftime("%Y-%m-%d") for i in date_range]

    out = pd.DataFrame()
    for i in date_range:
        try:
            df = getData(i)
        except:
            df = pd.DataFrame()
        out = pd.concat([out, df]) 
    out.to_csv("TraceBeefData.csv". index=False)

if __name__ == "__main__":
    main()
