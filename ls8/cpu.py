"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        pass
        # create 8 registers 1 - 8, need IM, IS, SP
        self.reg = [0b0] * 8

        # internal registers
        self.pc = 0  # Program counter = address of current_instructions
        self.ir = 0  # instruction register = contains copy of current_instructions
        self.mar = 0  # memory address register = holds memory address read/write
        self.mdr = 0  # memory data register = holds the value to write or value to read
        self.fl = 0  # flags

        self.ram = [0b0] * 255
        self.pc = 0

        # opcodes
        self.opcodes = {0b10000010: 'LDI', 0b01000111: 'PRN', 0b00000001: 'HLT'}

    def load(self):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True
        while running:
            command = self.ram[self.pc] # don't forget this again
            try:
                if self.opcodes[command] == 'LDI':
                    register = self.ram[self.pc+1]
                    val = self.ram[self.pc+2]
                    self.reg[register] = val
                    self.pc += 3
                elif self.opcodes[command] == 'PRN':
                    register = self.ram[self.pc+1]
                    val = self.reg[register]
                    print(val)
                    self.pc += 2
                elif self.opcodes[command] == 'HLT':
                    running = False

            except KeyError as e:
                print(f"Unknown Command {command}")
                self.pc += 1
        pass
    
    def ram_read(self, location):
        """Read to RAM"""
        return self.ram[location]

    def ram_write(self, location):
        """Write to RAM"""
        return self.ram[location]
