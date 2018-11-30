# Create Boxplots
def create_boxplots(df):
    import numpy as np
    import matplotlib.pyplot as plt
    
    cols = df.columns.tolist()[:-1]
    for col in cols:
        if(df[col].dtype in [np.int64, np.int32, np.float64]
            and df[col].name != "CreateColumnName"):
            fig = plt.figure(figsize = (6,6))
            fig.clf()
            ax = fig.gca()
            df.boxplot(column = [col], ax = ax, by = ['CreateColumnName'])
    return('Done')
create_boxplots(frame)