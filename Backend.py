# Contains all the encoding methods for ciphers
class Encoder:
    def __init__(self):
        print("Encoder Created")
        self.Output = ""
    # Gets the input to be encoded from a specified file.

    def Get_Input(self):
        return 0

    def Pad_Input(self):
        return 0

    def Ceaser_Encode(self, read_buffer, Key_Offset):
        for char in read_buffer:
            self.Output += chr(ord(char) + int(Key_Offset))

    def Vigenere_Encode(self, read_buffer, Key_buffer):
        count = 0
        self.Output = ""
        for Read_Char in read_buffer:
            # print("Readloop: Char = " + Read_Char) #Debugging print statement
            Key_Char = Key_buffer[count]
            count += 1
            # print("Key_Char = : " + Key_Char) #Debugging print statment
            if count == len(Key_buffer):
                count = 0
            self.Output += chr(ord(Read_Char) + int(ord(Key_Char)))

    def Physical_Shift_Encode(self,  read_buffer, shift_value):
        self.Output = ""
        count = 0
        while count < int(shift_value):
            count += 1

        while count < len(read_buffer):
            #print("Current char in read_buffer" + read_buffer[count])
            self.Output += read_buffer[count]
            count += 1
        count = 0
        while count < int(shift_value):
            #print("Current char in read_buffer" + read_buffer[count])
            self.Output += read_buffer[count]
            count += 1

    def Columnar_Encode(self):
        return 0

    def Block_Chain_Encode(self):
        pass

# Contains all the Decoder methods for each of the ciphers.


class Decoder:
    def __init__(self):
        print("Decoder Created\n")
        self.Output = ""
    # Writes the encoded output to a specified file.

    def Write_Output(self):
        return 0

    def Unpad_Input(self):
        padded_bytes = 0
        return padded_bytes

    def Ceaser_Decode(self, read_buffer, Key_Offset):
        for char in read_buffer:
            self.Output += chr(ord(char) - int(Key_Offset))

    def Vigenere_Decode(self, read_buffer, Key_buffer):
        count = 0
        self.Output = ""
        for Read_Char in read_buffer:
            # print("Readloop: Char = " + Read_Char) #Debugging print statement
            Key_Char = Key_buffer[count]
            count += 1
            # print("Key_Char = : " + Key_Char)#Debugging print statement
            if count == len(Key_buffer):
                count = 0
            self.Output += chr(ord(Read_Char) - int(ord(Key_Char)))

    def Physical_Shift_Decode(self, read_buffer, shift_value):
        count = 0
        self.Output = ""
        #print(len(read_buffer) - int(shift_value))
        while count < len(read_buffer) - int(shift_value):
            count += 1
        while count < len(read_buffer):
            #print("Current char in read_buffer " + read_buffer[count])
            self.Output += read_buffer[count]
            count += 1
        count = 0
        while count < len(read_buffer) - int(shift_value):
            #print("Current char in read_buffer " + read_buffer[count])
            self.Output += read_buffer[count]
            count += 1

    def Columnar_Decode(self):
        return 0

    def Block_Chain_Decode(self):
        pass

# Responsible for handling the order of ciphers in a product cipher.


class Product:

    def __init__(self):
        self.Product_List = []
        self.Rounds = 1
        self.Decode = False

    def add(self, encode_name):
        pass

    def remove(self, encode_name):
        pass

    def view(self):
        print(self.Product_List)

    def clear(self):
        self.Product_List = []
        self.Rounds = 1
        self.Decode = False

    def set_rounds(self, New_Rounds):
        self.Rounds = New_Rounds

# Responsible for creating the various buffers that we may need.


class Buffer:
    def __init__(self):
        buffer = []

    def Convert_To_List(self, Input):
        self.buffer = []
        count = 0
        for char in Input:
            self.buffer.append(char)
            count += 1
        self.length = count
        return self.buffer

    def Get_Element(self, Index):
        return self.buffer[Index]

    def Print_Buffer(self):
        print(self.buffer)
