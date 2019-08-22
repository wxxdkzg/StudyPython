import OpenOPC  #导入模块
opc = OpenOPC.client()
opc.servers()   #列出本机中所有opc server清单
#[u'Takebishi.Melsec.1']  # 返回的，opc server名称
opc.connect(u'Takebishi.Melsec.1') #从opc server清单中选择需要连接的服务
opc.read('PLC1.A01.BldCntL')  #读取指定设备Device，组Group，标签Tag的数据