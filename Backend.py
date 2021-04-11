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

    def Ceaser_Encode(self, read_buffer, Key_Offset, Dim, Rounds, write_buffer):
        Dim = int(Dim)
        RoundCount = 0
        count = 0

        x = 0
        y = 0

        while RoundCount < int(Rounds):
            while count < Dim * Dim:
                write_buffer[x][y] = chr(
                    ord(read_buffer[x][y]) + int(Key_Offset))
                if x < Dim - 1 and y < Dim - 1:
                    y += 1
                elif x < Dim - 1 and y == Dim - 1:
                    x += 1
                    y = 0
                elif x == Dim - 1 and y < Dim - 1:
                    y += 1
                count += 1
            RoundCount += 1
            print("Round: " + str(RoundCount))
            Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                write_buffer = self.Empty_Buffer(Dim)
                x = 0
                y = 0
                count = 0
        return write_buffer

    def Vigenere_Encode(self, read_buffer, Key_buffer, Dim, Rounds, write_buffer):
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

    def Physical_Shift_Encode(self,  read_buffer, shift_value, Dim, Rounds, write_buffer):
        Dim = int(Dim)
        RoundCount = 0
        count = 0

        read_x = 0  # X var for read buffer
        read_y = 0  # Y var for read buffer
        write_x = 0  # X var for write buffer
        write_y = 0  # Y var for write buffer

        while RoundCount < int(Rounds):
            while count < int(shift_value):
                # Start traversing read_buffer.
                if read_x < Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x < Dim - 1 and read_y == Dim - 1:
                    read_x += 1
                    read_y = 0
                elif read_x == Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                count += 1
            # Write the rest of the text from the buffer into the output buffer.
            while count < (Dim * Dim):
                write_buffer[write_x][write_y] = read_buffer[read_x][read_y]
                # Adjust read buffer x and y vars.
                if read_x < Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x < Dim - 1 and read_y == Dim - 1:
                    read_x += 1
                    read_y = 0
                elif read_x == Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x == Dim - 1 and read_y == Dim - 1:
                    read_x = 0
                    read_y = 0
                # Adjust write buffer x and y vars.
                if write_x < Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                elif write_x < Dim - 1 and write_y == Dim - 1:
                    write_x += 1
                    write_y = 0
                elif write_x == Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                count += 1
            count = 0
            while count < int(shift_value):
                write_buffer[write_x][write_y] = read_buffer[read_x][read_y]
                # Adjust read buffer x and y vars.
                if read_x < Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x < Dim - 1 and read_y == Dim - 1:
                    read_x += 1
                    read_y = 0
                elif read_x == Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x == Dim - 1 and read_y == Dim - 1:
                    read_x = 0
                    read_y = 0
                # Adjust write buffer x and y vars.
                if write_x < Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                elif write_x < Dim - 1 and write_y == Dim - 1:
                    write_x += 1
                    write_y = 0
                elif write_x == Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                count += 1
            RoundCount += 1
            print("Round: " + str(RoundCount))
            Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                write_buffer = self.Empty_Buffer(Dim)
                read_x = 0
                read_y = 0
                write_x = 0
                write_y = 0
                count = 0
        return write_buffer

    def Columnar_Encode(self):
        return 0

    def Block_Chain_Encode(self):
        pass

    def Empty_Buffer(self, Dim):
        Dim = int(Dim)
        buffer = [[0] * Dim]
        i = 1
        # Create a (Dim x Dim) matrix.
        while i < Dim:
            buffer.append([0] * Dim)
            i += 1
        return buffer

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

    def Ceaser_Decode(self, read_buffer, Key_Offset, Dim, Rounds, write_buffer):
        Dim = int(Dim)
        RoundCount = 0
        count = 0

        x = 0
        y = 0

        while RoundCount < int(Rounds):
            while count < Dim * Dim:
                write_buffer[x][y] = chr(
                    ord(read_buffer[x][y]) - int(Key_Offset))
                if x < Dim - 1 and y < Dim - 1:
                    y += 1
                elif x < Dim - 1 and y == Dim - 1:
                    x += 1
                    y = 0
                elif x == Dim - 1 and y < Dim - 1:
                    y += 1
                count += 1
            RoundCount += 1
            print("Round: " + str(RoundCount))
            Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                #write_buffer = self.Empty_Buffer(Dim)
                x = 0
                y = 0
                count = 0
        return write_buffer

    def Vigenere_Decode(self, read_buffer, Key_buffer, Dim, Rounds, write_buffer):
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

    def Physical_Shift_Decode(self, read_buffer, shift_value, Dim, Rounds, write_buffer):
        Dim = int(Dim)
        RoundCount = 0
        count = 0

        read_x = 0  # X var for read buffer
        read_y = 0  # Y var for read buffer
        write_x = 0  # X var for write buffer
        write_y = 0  # Y var for write buffer

        # self.Output = "" #Depricated
        # While we are not on the last round.
        while RoundCount < int(Rounds):
            # Shift to the new start.
            while count < ((Dim * Dim) - int(shift_value)):
                # Start traversing read_buffer.
                if read_x < Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x < Dim - 1 and read_y == Dim - 1:
                    read_x += 1
                    read_y = 0
                elif read_x == Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                count += 1
            # Write the rest of the text from the buffer into the output buffer.
            while count < (Dim * Dim):
                # Copy read buffer element into write buffer at the correct place.
                write_buffer[write_x][write_y] = read_buffer[read_x][read_y]
                # Adjust read buffer x and y vars.
                if read_x < Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x < Dim - 1 and read_y == Dim - 1:
                    read_x += 1
                    read_y = 0
                elif read_x == Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x == Dim - 1 and read_y == Dim - 1:
                    read_x = 0
                    read_y = 0
                # Adjust write buffer x and y vars.
                if write_x < Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                elif write_x < Dim - 1 and write_y == Dim - 1:
                    write_x += 1
                    write_y = 0
                elif write_x == Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                count += 1
            count = 0
            while count < ((Dim * Dim) - int(shift_value)):
                write_buffer[write_x][write_y] = read_buffer[read_x][read_y]
                # Adjust read buffer x and y vars.
                if read_x < Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x < Dim - 1 and read_y == Dim - 1:
                    read_x += 1
                    read_y = 0
                elif read_x == Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x == Dim - 1 and read_y == Dim - 1:
                    read_x = 0
                    read_y = 0
                # Adjust write buffer x and y vars.
                if write_x < Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                elif write_x < Dim - 1 and write_y == Dim - 1:
                    write_x += 1
                    write_y = 0
                elif write_x == Dim - 1 and write_y < Dim - 1:
                    write_y += 1
                count += 1
            RoundCount += 1
            print("Round: " + str(RoundCount))
            Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                read_x = 0
                read_y = 0
                write_x = 0
                write_y = 0
                count = 0
        return write_buffer

    def Columnar_Decode(self):
        return 0

    def Block_Chain_Decode(self):
        pass

# Responsible for handling the order of ciphers in a product cipher.


class Product:

    def __init__(self):
        self.Product_List = []
        self.Rounds = 1
        self.Decode = True
        self.Dim = 2  # Dimension of the buffers.

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

    def set_dim(self, New_Dim):
        self.Dim = New_Dim

# Responsible for creating the various buffers that we may need.


class Buffer:
    def __init__(self):
        self.buffer = []

    def Convert_To_List(self, Input, Dim):
        self.buffer = [[0] * int(Dim)]
        i = 1
        # Create a (Dim x Dim) matrix.
        while i < int(Dim):
            self.buffer.append([0] * int(Dim))
            i += 1
        count = 0
        x = 0
        y = 0
        for char in Input:
            self.buffer[x][y] = char
            if x < int(Dim) - 1 and y < int(Dim) - 1:
                y += 1
                count += 1
            elif x < int(Dim) - 1 and y == int(Dim) - 1:
                x += 1
                y = 0
                count += 1
            elif x == int(Dim) - 1 and y < int(Dim) - 1:
                y += 1
                count += 1
        self.length = count
        return self.buffer

    def Get_Element(self, Index):
        return self.buffer[Index]

    def Print_Buffer(self, Dim, buffer):
        Dim = int(Dim)
        count = 0
        Output = ""
        x = 0
        y = 0
        while count < Dim * Dim:
            char = buffer[x][y]
            Output += str(char)
            if x < Dim - 1 and y < Dim - 1:
                y += 1
            elif x < Dim - 1 and y == Dim - 1:
                x += 1
                y = 0
            elif x == Dim - 1 and y < Dim - 1:
                y += 1
            count += 1
        print("Output: " + Output)


Buffers = Buffer()
