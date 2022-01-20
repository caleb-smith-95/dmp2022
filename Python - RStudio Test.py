
import pandas as pd
passing01 = pd.read_excel('C:/Users/caleb/Documents/R Datasets/Masters Project/Clean Data/Passing/2001 Passing.xlsx', engine = 'openpyxl')
passing02 = pd.read_excel('C:/Users/caleb/Documents/R Datasets/Masters Project/Clean Data/Passing/2002 Passing.xlsx', engine = 'openpyxl')
passing03 = pd.read_excel('C:/Users/caleb/Documents/R Datasets/Masters Project/Clean Data/Passing/2003 Passing.xlsx', engine = 'openpyxl')
passing04 = pd.read_excel('C:/Users/caleb/Documents/R Datasets/Masters Project/Clean Data/Passing/2004 Passing.xlsx', engine = 'openpyxl')
passing05 = pd.read_excel('C:/Users/caleb/Documents/R Datasets/Masters Project/Clean Data/Passing/2005 Passing.xlsx', engine = 'openpyxl')

passing01_clean = passing01.copy().drop('Rk', axis=1)
passing02_clean = passing02.copy().drop('Rk', axis=1)
passing03_clean = passing03.copy().drop('Rk', axis=1)
passing04_clean = passing04.copy().drop('Rk', axis=1)
passing05_clean = passing05.copy().drop('Rk', axis=1)

passing01_clean['Year'] = 2001
passing02_clean['Year'] = 2002
passing03_clean['Year'] = 2003
passing04_clean['Year'] = 2004
passing05_clean['Year'] = 2005

comb_passing = pd.concat([passing01_clean, passing02_clean, passing03_clean, passing04_clean, passing05_clean], ignore_index=True)

comb_passing['Name'] = comb_passing['Player']

for i in range(0, len(comb_passing), 1):
  comb_passing['Name'][i] = comb_passing['Name'].str.split('*')[i][0]
comb_passing_clean = comb_passing.reindex(columns=['Name', 'Year', 'Age', 'Tm', 'G', 'GS', 'Cmp', 'Att', 'Cmp%', 'Yds', 'TD', 'Int', 'Y/A', 'Y/C', 'Rate']).copy()


