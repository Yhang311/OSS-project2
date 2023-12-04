#1.Print the top 10 players in hits (안타, H), batting average (타율, avg), homerun (홈런, HR),
#  and on base percentage (출루율, OBP) for each year from 2015 to 2018.

import pandas as pd

def get_top10(source):
    df=pd.read_csv('./2019_kbo_for_kaggle_v2.csv')

    year = (df['p_year'] == 2015) |(df['p_year'] == 2016) | (df['p_year'] == 2017) |(df['p_year'] == 2018) 
    selected = df[year]

    res = selected[['batter_name',source]]

    sort = res.sort_values(by=source,ascending=False)
    top10 = sort.head(10)
    print(source)
    print(top10[['batter_name',source]])
    
#Print Start
# H
top10 = get_top10('H')

# avg
top10 = get_top10('avg')

# HR
top10 = get_top10('HR')

# OBP
top10 = get_top10('OBP')


#2.Print the player with the highest war (승리 기여도) by position (cp) in 2018. 
def bestwarname(source):
    df=pd.read_csv('./2019_kbo_for_kaggle_v2.csv')
    
    condition = (df['p_year'] == 2018) & (df['cp'] == source)
    
    res = df.loc[condition,['batter_name','war']]
    top1 = res.loc[res['war'].idxmax()]
    print(source)
    print(top1)
    
top1 = bestwarname('포수')

top1 = bestwarname('1루수')

top1 = bestwarname('2루수')

top1 = bestwarname('3루수')

top1 = bestwarname('유격수')

top1 = bestwarname('좌익수')

top1 = bestwarname('중견수')

top1 = bestwarname('우익수')


#3.Among R (득점), H (안타), HR (홈런), RBI (타점), SB (도루), war (승리 기여도), avg (타율), OBP 
#(출루율), and SLG (장타율), which has the highest correlation with salary (연봉)?

df=pd.read_csv('./2019_kbo_for_kaggle_v2.csv')

type = ['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']
setdf = df[type]

type_matrix = setdf.corr()
correlation = type_matrix['salary'].drop('salary')
highest_correlation = correlation.abs().idxmax()
highest_correlation_value = correlation.abs().max()

print(f"the highest correlation with salary is  '{highest_correlation}'，the highest correlation value is {highest_correlation_value:.2f}。")