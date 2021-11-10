# import os
# lstName = ["25","26","27","35","36","37","45","46","47"]
# for i in lstName:
# #    i+=1  Quick_Any2Ico.exe "-img=未标题-1.png" "icon=hhh.ico"
#     os.system("mv %s.ico %s/yph.ico" % (i,i))
import os

root = os.path.abspath('.')[:1] #获取当前目录所在硬盘的根目录
strValue='''
[{000214A0-0000-0000-C000-000000000046}]
Prop3=19,11
[InternetShortcut]
IDList=
URL=https://wangying.yangpenghe.ml/
IconIndex=0
HotKey=0
IconFile=%s:\\YY.ico
''' % (root)
ipt = open("YY.url","w")
ipt.write(strValue)
ipt.close()
os.system("attrib +s +a +h +r YY.ico")
os.system("pause")


cmd1 = '''
attrib +s +a +h +r autorun.inf
'''
# print(strValue)
