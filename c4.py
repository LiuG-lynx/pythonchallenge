# 输入某年某月某日，判断这一天是这一年的第几天？
import datetime
ndt = str(input('输入的时间(201512110):'))
dt = datetime.datetime.strptime(ndt, '%Y%m%d')  #转换成  datetine.datetime类型 用以运算
print('dt:',dt,type(dt)) #、
anthor_ndt = ndt[:4] + '0101'  # 利用切片获取 当前年份的 第一天的 str格式
anthor_dt = datetime.datetime.strptime(anthor_ndt, '%Y%m%d') #转换成  datetine.datetime类型 用以运算

print((dt-anthor_dt).days + 1)  # (dt-anthor_dt) 获取天数