import argparse

from cpu import CPU
from instruction import LDAInstruction
from rom import ROM


def main():
    # Setup Command Line Argument Parser
    parser = argparse.ArgumentParser(description='NES Emulator.')
    parser.add_argument('rom_path',
                        metavar='RomPath',
                        type=str,
                        help='path to nes rom')

    args = parser.parse_args()

    with open(args.rom_path, 'rb') as file:
        rom_bytes = file.read()

    rom = ROM(rom_bytes)

    # create CPU
    cpu = CPU()
    cpu.run_rom(rom)

if __name__ == '__main__':
    main()
