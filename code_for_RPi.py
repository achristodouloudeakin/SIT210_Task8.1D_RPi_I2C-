from smbus import SMBus

addr = 0x8
bus = SMBus(1)
program_exist = 1

print("Enter 1 for ON, or 0 for OFF, enter any other value to shut-down program")

while program_exist == 1:

    ledstate = input(">>>>>   ")
    
    if ledstate == "1":
        bus.write_byte(addr, 0x1)
    elif ledstate == "0":
        bus.write_byte(addr, 0x0)
    else:
        print("Shutting Down")
        bus.write_byte(addr, 0x0)
        program_exist == 0
