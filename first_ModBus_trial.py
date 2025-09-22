import pymodbus

from pymodbus.client import ModbusTcpClient as ModbusClient

from pymodbus.exceptions import ConnectionException

client = ModbusClient('192.168.127.254', port=502)

try:
    #connect to the devices
    client.connect()
    print("connected to Moxa 1240 device")
    
    
    # Read holding registers
    
    result = client.read_holding_registers(address=24, count=8) # Bunu 24 yapıca çalışmış
    
    if result.isError():
        print("An error reading holding register")
        
    else:
        print("Registers Values:",result.registers)
        
        
        
        
    client.close()
    
    print("Dsiconnected from Moxa 1240device")
    
except ConnectionException as ex:
    print("Connection failed",ex)
    
except Exception as ex:
    
    print("An Error acured:",ex)
    
