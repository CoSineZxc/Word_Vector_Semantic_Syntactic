from openpyxl import load_workbook
import pandas as pd

exp=[]
part=[]
cond=[]
trial=[]
r=[]
for i in range(2):
    for j in range(4):
        wb=load_workbook('./cross_correlation_rslt/Exp'+str(i+1)+'_'+chr(ord('A')+j)+'_r.xlsx')
        sheets = wb.worksheets
        sheet1 = sheets[0]
        col_exp=[]
        for col in sheet1['E']:
            col_exp.append(col.value)
        exp+=col_exp[1:]
        col_part=[]
        for col in sheet1['D']:
            if i==0 or col.value=='Var4':
                col_part.append(col.value)
            else:
                col_part.append(str(int(col.value)+23))
        part+=col_part[1:]
        col_cond=[]
        for col in sheet1['C']:
            col_cond.append(col.value)
        cond+=col_cond[1:]
        col_trial=[]
        for col in sheet1['A']:
            if i==0:
                col_trial.append('A'+col.value)
            else:
                col_trial.append('B' + col.value)
        trial += col_trial[1:]
        col_r=[]
        for col in sheet1['B']:
            col_r.append(col.value)
        r+=col_r[1:]


dataframe = pd.DataFrame({'exp':exp,'part':part,'cond':cond,'trial':trial,'R':r})
dataframe.to_csv("all_r_ANOVA.csv",index=False,sep=',')