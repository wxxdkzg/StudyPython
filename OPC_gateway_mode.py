import OpenOPC

gateway = '192.168.1.90'
opchost = 'testbox'

opcserv = 'KEPware.KEPServerEx.V4'
taglist = ['Channel_4.Device_6.Bool_15']
print('Connecting to Gateway Server on: ', gateway)
opc = OpenOPC.open_client(gateway)
opc.connect(opcserv)
v = opc.read(taglist)
opc.close()
for i in range(len(v)):
    (name,val,qual,time) = v[i]
    print('%-15s %-15s %-15s %-15s'%(name,val,qual,time))