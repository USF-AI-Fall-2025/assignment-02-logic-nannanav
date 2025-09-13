import pandas as pd

class DataInvestigator:

    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a pandas dataframe")
        
        if df.empty:
            raise ValueError("Dataframe cannot be empty")

        self.df = df

    def baseline(self, col):
        if self.df is None or self.df.empty:
            return None
        
        try:
            column_data = self.df.iloc[:, col]

            mode_result = column_data.mode()

            return mode_result.iloc[0]
        except:
            return None

    def corr(self, col1, col2):
        if self.df is None or self.df.empty:
            return None
        
        try:
            column1 = self.df.iloc[:, col1]
            column2 = self.df.iloc[:, col2]

            correlation = column1.corr(column2)

            if pd.isna(correlation):
                return None
            
            return correlation
        except:
            return None

    def zeroR(self, col):
        if self.df is None or self.df.empty:
            return None
        
        try:
            column_data = self.df.iloc[:, col]

            mode_result = column_data.mode()

            return mode_result.iloc[0]
        except:
            return None

