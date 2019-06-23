from collections import defaultdict

from instruction import *
from rom import ROM


class CPU(object):
    def __init__(self):
        # TODO: proper registers
        self.registers = []
        self.running = True

        # prgram counter stores current execution point
        self.pc = None

        self.instruction_classes = [
            SEIInstruction,
            LDAInstruction,
            CLDInstruction
        ]

        self.instruction_class_mapping = defaultdict()
        for instruction_class in self.instruction_classes:
            self.instruction_class_mapping[instruction_class.identifier_byte] = instruction_class

        self.rom = None

    def run_rom(self, rom: ROM):
        # load rom
        self.rom = rom
        self.pc = self.rom.header_size

        # run program
        self.running = True
        while self.running:
            # get the current byte at pc
            identifier_byte = self.rom.get_byte(self.pc)

            # turn the byte into an Instruction
            instruction_class = self.instruction_class_mapping.get(identifier_byte, None)

            if instruction_class is None:
                raise Exception("Instruction Not Found [0x{}]".format(identifier_byte.hex()))

            instruction = instruction_class()
            instruction.execute()

            self.pc += instruction.instruction_length

    def process_instructions(self, instructions: bytes):
        pass

    def process_instruction(self, instruction: Instruction):
        #TODO: process the instruction
        instruction.process()
