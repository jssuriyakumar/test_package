import pandas as pd

class Test:
    def __init__(self):
        pass
    def test(self):
        l = [1,2,3,4]
        df = pd.DataFrame(l,columns = ['numbers'])
        return df
