import time

#YES ITS THE CLOCK
class clock:
    def __init__(self):
        self.frequency = 100

#Control Unit it has two registers A,B
class CU:
    def __init__(self):
        self.A = 0
        self.B = 0

    def ADD(self):
        alu.ADD()

    def SUB(self):
        alu.SUB()

    def MUL(self):
        alu.MUL()
    
    def LDA(self,index):
        self.A = ram.ram[index]

    def LDB(self,index):
        self.B = ram.ram[index]

    def LD1(self,index):
        alu.R1 = ram.ram[index]

    def LD2(self,index):
        alu.R2 = ram.ram[index]

    def LD3(self,index):
        alu.R3 = ram.ram[index]

    def LD4(self,index):
        ram.Load(index)

    def JMP(self,index):
        pc.pcV = index+1
        pc.pcOP = index
    
    def ReadOPcode(self):
        value = ram.ram[pc.pcV]
        opcode = ram.ram[pc.pcOP]
        if opcode == 1: self.ADD()
        if opcode == 2: self.SUB()
        if opcode == 3: self.MUL()
        if opcode == 4: self.LDA(value)
        if opcode == 5: self.LDB(value)
        if opcode == 6: self.LD1(value)
        if opcode == 7: self.LD2(value)
        if opcode == 8: self.LD3(value)
        if opcode == 9: self.LD4(value)
        if opcode == 10: self.JMP(value)

#Creates the ram 256 Bytes
class Ram:
    def  __init__(self):
        self.ram = []
        self.Reg4 = 0
        for line in range(256):
            self.ram.append(0)

    def Store(self,index,value):
        self.ram[index] = value

    def Load(self,index):
        self.Reg4 = self.ram[index]

#it has 3 functions add and subtract and multiply
class ALU:
    def __init__(self):
        self.R1 = 0
        self.R2 = 0
        self.R3 = 0
        
    def ADD(self):
        self.R1 = self.R1 + self.R2
    
    def SUB(self):
        self.R1 = self.R1 - self.R2

    def MUL(self):
        self.R1 = self.R1 * self.R2

#it counts :O
class PC:
    def __init__(self):
        self.pcV = 0
        self.pcOP = -1
    def inc(self):
        self.pcV += 2
        self.pcOP += 2

pc = PC()
ram = Ram()
alu = ALU()
cu = CU()
c = clock()
##ram coder``
f = open("Ram.txt", "r")
Lines = f.readlines()
for i in range(len(Lines)):
    Lines[i] = Lines[i].replace("\n","")
for i in range(len(Lines)):
    ram.Store(i,int(Lines[i]))


while 1:
    pc.inc()
    cu.ReadOPcode()
    print("A:",cu.A,"B:",cu.B,"1:",alu.R1,"2:",alu.R2,"3:",alu.R3,"4:",ram.Reg4,"VALUE:",pc.pcV,"OPCODE:",pc.pcOP)
    print(ram.ram[pc.pcOP],ram.ram[pc.pcV])
    # print(alu.R1)
    time.sleep(1/c.frequency)



        