
import pandas as pd

file1 = pd.read_csv('zwayam.csv')
new_file = file1.drop(columns=['Designation ID','Function','Subtrack','Job Code','Concat Value','Track','Effective date'])

list1 = ['Finance & Secretarial']
new_table = new_file[new_file['Grade'] == '1.3']
print(new_table)

file2 = pd.read_csv('newprod.csv',encoding='latin1')

new_file2 = file2.drop(columns = ['company_id','parent','productName','lastUpdatedTime','isActive','id','type'])
# new_file2.columns = []
# print(new_file2.head(2))
# print(new_file2.columns)
new_file2.columns =  ['Grade','Job Group','Job Family','Job Titles']
# print(new_file2.head(2))

# one = new_file2[new_file2['Job Family'] == 'Marketing']
# print(one)
print("====================================================================================================")
new_table3 = new_file2[(new_file2['Job Family'] == "Enabling") & new_file2['Grade'] == '1.3']
# print(new_table3)
new_tablex = new_file2[new_file2['Grade'] == '1.3']
print(new_table)

merge_file = new_file2.merge(new_file)
print(merge_file)


