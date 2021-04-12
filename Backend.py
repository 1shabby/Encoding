# Contains all the encoding methods for ciphers
class Encoder:
    def __init__(self):
        self.Buffer = []

    def Pad_Input(self):
        return 0

    def Ceaser_Encode(self, read_buffer, write_buffer, Key_Offset, Dim, Rounds, round_Count):
        Dim = int(Dim)
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
            #print("Round: " + str(RoundCount))
            #Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                write_buffer = Empty_Buffer(Dim)
                x = 0
                y = 0
                count = 0
        self.Buffer = write_buffer

    def Vigenere_Encode(self, read_buffer, Key_buffer, write_buffer, key_length, Dim, Rounds, round_Count):
        Dim = int(Dim)
        count = 0
        key_count = 0

        read_x = 0
        read_y = 0
        key_x = 0
        key_y = 0

        while RoundCount < int(Rounds):
            while count < Dim * Dim:
                write_buffer[read_x][read_y] = ord(
                    read_buffer[read_x][read_y]) + ord(Key_buffer[key_x][key_y])
                write_buffer[read_x][read_y] = chr(
                    write_buffer[read_x][read_y])
                if read_x < Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                elif read_x < Dim - 1 and read_y == Dim - 1:
                    read_x += 1
                    read_y = 0
                elif read_x == Dim - 1 and read_y < Dim - 1:
                    read_y += 1
                count += 1
                if key_count < key_length:
                    if key_x < Dim - 1 and key_y < Dim - 1:
                        key_y += 1
                    elif key_x < Dim - 1 and key_y == Dim - 1:
                        key_x += 1
                        key_y = 0
                    elif key_x == Dim - 1 and key_y < Dim - 1:
                        key_y += 1
                    elif key_x == Dim - 1 and key_y == Dim - 1:
                        key_x = 0
                        key_y = 0
                else:
                    key_x = 0
                    key_y = 0
                key_count += 1
            RoundCount += 1
            #print("Round: " + str(RoundCount))
            #Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                write_buffer = Empty_Buffer(Dim)
                x = 0
                y = 0
                count = 0
        self.Buffer = write_buffer

    def Physical_Shift_Encode(self,  read_buffer, write_buffer, Dim, shift_value, Rounds, round_Count):
        Dim = int(Dim)
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
            #print("Round: " + str(RoundCount))
            #Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                write_buffer = Empty_Buffer(Dim)
                read_x = 0
                read_y = 0
                write_x = 0
                write_y = 0
                count = 0
        self.Buffer = write_buffer

    def Columnar_Encode(self):
        return 0

    def Block_Chain_Encode(self):
        pass

# Contains all the Decoder methods for each of the ciphers.


class Decoder:
    def __init__(self):
        self.Buffer = []
    # Writes the encoded output to a specified file.

    def Write_Output(self):
        return 0

    def Unpad_Input(self):
        padded_bytes = 0
        return padded_bytes

    def Ceaser_Decode(self, read_buffer, write_buffer, Dim, Key_Offset, Rounds, round_Count):
        Dim = int(Dim)
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
            # print("Round: " + str(RoundCount))
            # Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                x = 0
                y = 0
                count = 0
        return write_buffer

    def Vigenere_Decode(self, read_buffer, Key_buffer, write_buffer, Dim, Rounds, round_Count):
        Dim = int(Dim)
        count = 0

        x = 0
        y = 0
        while RoundCount < int(Rounds):
            while count < Dim * Dim:
                write_buffer[x][y] = ord(
                    read_buffer[x][y]) - ord(Key_buffer[x][y])
                write_buffer[x][y] = chr(write_buffer[x][y])
                if x < Dim - 1 and y < Dim - 1:
                    y += 1
                elif x < Dim - 1 and y == Dim - 1:
                    x += 1
                    y = 0
                elif x == Dim - 1 and y < Dim - 1:
                    y += 1
                count += 1
            RoundCount += 1
            # print("Round: " + str(RoundCount))
            # Buffers.Print_Buffer(Dim, write_buffer)
            if RoundCount < int(Rounds):
                read_buffer = write_buffer
                x = 0
                y = 0
                count = 0
        return write_buffer

    def Physical_Shift_Decode(self, read_buffer, shift_value, Dim, Rounds, write_buffer, round_Count):
        Dim = int(Dim)
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
        self.Round_Count = 0
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
        self.input_length = 0

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
            elif x < int(Dim) - 1 and y == int(Dim) - 1:
                x += 1
                y = 0
            elif x == int(Dim) - 1 and y < int(Dim) - 1:
                y += 1
            count += 1
            self.input_length += 1

    def Get_Element(self, Index):
        return self.buffer[Index]

    def Print_Buffer(self, Dim):
        Dim = int(Dim)
        count = 0
        Output = ""
        x = 0
        y = 0
        while count < Dim * Dim:
            char = self.buffer[x][y]
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


def Empty_Buffer(Dim):
    buffer = []
    i = 1
    # Create a (Dim x Dim) matrix.
    while i < int(Dim):
        self.buffer.append([0] * int(Dim))
        i += 1
        count = 0
        x = 0
        y = 0
    return buffer
