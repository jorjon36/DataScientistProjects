# Create Faceted Histograms
%matplotlib inline

import seaborn as sns
sns.set_style("whitegrid")

def create_facethists(df):
	import numpy as np
	cols = df.columns.tolist()[:-1]
	for col in cols:
		if(df[col].dtype in [np.int64, np.int32, np.float64]
			and df[col].name != "CreateColumnName"):
			g = sns.FacetGrid(frame, col="CreateColumnName")
			g.map(sns.distplot, col)
	return('Done')

create_facethists(frame)