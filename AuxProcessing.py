#!/usr/bin/env python3

# Import required packages
from dotenv import load_dotenv
import binascii
import os

load_dotenv()  # Load environment variables from .env file


class AuxProcessing:

    @staticmethod
    def IntegersToBinary(integer_representation) -> str:
        '''Converts integer representation to binary representation using a 4-bit format per integer'''
        return str(''.join([((int(os.environ['ENTRY_LENGTH']) - len(bin_value)) * '0') + bin_value for bin_value in [bin(int(character))[2:] for character in str(integer_representation)]]))

    @staticmethod
    def BinaryToIntegers(binary_representation) -> int:
        '''Converts binary representation to integer representation using a nibble format'''
        return int(''.join([str(int(binary_representation[index:index+4], 2)) for index in range(0, len(binary_representation), 4)]))

    @staticmethod
    def UTF8ToBinary(utf8_representation, encoding='utf-8', errors='surrogatepass') -> str:
        '''Converts UTF-8 representation to binary representation using 8-bit format'''
        bits = bin(int(binascii.hexlify(
            utf8_representation.encode(encoding, errors)), 16))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    @staticmethod
    def BinaryToUTF8(binary_representation, encoding='utf-8', errors='surrogatepass') -> str:
        '''Converts binary representation to UTF-8 representation'''
        return AuxProcessing.IntegerToBytes(int(binary_representation, 2)).decode(encoding, errors)

    @staticmethod
    def IntegerToBytes(integer_representation) -> bytes:
        '''Converts integer representation to byte representation'''
        hex_string = '%x' % integer_representation
        number = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(number + (number & 1)))
