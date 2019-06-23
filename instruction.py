from abc import ABC, abstractmethod


class Instruction(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        return 'Undefined'

    @property
    @abstractmethod
    def identifier_byte(self) -> bytes:
        return None

    @property
    @abstractmethod
    def instruction_length(self) -> int:
        return 1

    @abstractmethod
    def execute(self):
        print(self.__str__())

    def __str__(self) -> str:
        return "{}, Identifier byte: {}".format(self.name, self.identifier_byte.hex())


class LDAInstruction(Instruction):
    name = 'LDA #'
    identifier_byte = bytes.fromhex('A9')
    instruction_length = 2

    def execute(self):
        super().execute()


class SEIInstruction(Instruction):
    name = 'SEI'
    identifier_byte = bytes.fromhex('78')
    instruction_length = 1

    def execute(self):
        super().execute()


class CLDInstruction(Instruction):
    name = 'CLD #'
    identifier_byte = bytes.fromhex('D8')
    instruction_length = 1

    def execute(self):
        super().execute()