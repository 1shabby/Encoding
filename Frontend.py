from Backend import Encoder, Decoder, Buffer, Product


def Info_Screen():
    print("The Ceaser Cipher is a very old encryption algorithm that relies upon shifting each characted by a given value.\n")
    print("The Vigenere Cipher is an extension of the Ceaser cipher. The difference is that\n"
          "we are given a string key and then we take the ascii value of the key char and add\n"
          "it onto the ascii value of the input char resulting in a new char which is our encoded\n"
          "text.\n")
    print("The Physical Shift cipher is quite a basic one as it does exactly what the name\n"
          "suggests. We take an input, then we take in a shift value like the Ceaser cipher\n"
          "but instead of changing the char, we just change its position so that all of the\n"
          "chars have an offset of 'shift' places.\n")


def Config():
    check = True
    while check == True:
        print("Config")
        print("Buffer Dimension: " + str(Product_Queue.Dim))
        print("Rounds: " + str(Product_Queue.Rounds))
        print("Decode: " + str(Product_Queue.Decode))
        print("\nD: Change Dim")
        print("R: Change rounds")
        print("M: Change decode mode (t/f)")
        print("B: Back\n")
        feedback = input(
            "Please enter a command from above to modify the settings, or exit the menu.")
        if feedback.upper() == 'D':
            feedback = input(
                "Please enter a new dimension for the buffers.\n")
            Product_Queue.set_dim(feedback)
        elif feedback.upper() == 'R':
            feedback = input(
                "Please enter an integer rounds that you would like to have a cipher run.\n")
            Product_Queue.set_rounds(feedback)
        elif feedback.upper() == 'M':
            feedback = input(
                "Please enter either 'enable' or 'disable' to enable/ disable decoding.\n")
            Product_Queue.set_decode(feedback)
        elif feedback.upper() == 'B':
            check = False


def Product_Menu():
    print("Product List Options")
    print("A: Add a cipher to the product list")
    print("R: Remove a cipher from the product list")
    print("P: Print the product list")
    print("C: Clear the Product list")
    print("X: Execute the product list")
    print("S: Settings")
    print("I: Cipher Information")
    print("B: Back\n")


def Product_Input_Handling():
    check = True
    while check == True:
        feedback = input("Please enter one of the commands above.\n")
        if feedback.upper() == 'A':
            print("Add to product list")
            Product_Add_Menu()

        elif feedback.upper() == 'R':
            print("Remove from list")
            Product_Remove_Menu()
        elif feedback.upper() == "P":
            print("Product list:")
            Product_Queue.view()
            Product_Queue.key_view()
        elif feedback.upper() == 'C':
            print("Clear list")
            Product_Queue.clear()
            Read_buffer.Input_to_List(Read_buffer.input)
            Read_buffer.List_To_Buffer(Product_Queue.Dim)
            Read_buffer.Print_Buffer(Product_Queue.Dim)
        elif feedback.upper() == 'X':
            print("Executing list...")
            Product_Execute()
        elif feedback.upper() == 'S':
            Config()
        elif feedback.upper() == 'I':
            Info_Screen()
        elif feedback.upper() == 'B':
            check = False
        Product_Menu()


def Product_Add_Menu():
    check = True
    index = 0
    key = "None"

    while check:
        feedback = input(
            "Please enter one of the following: 'Ceaser', 'Vigenere', or 'Physical', and press enter.\n")
        if feedback.lower() == 'ceaser' or feedback.lower() == 'c':
            Operation = 'Ceaser'
            feedback = input(
                "Please enter an integer you would like to shift by.\n")
            key = int(feedback)
            check = False
        elif feedback.lower() == 'vigenere' or feedback.lower() == 'v':
            Operation = 'Vigenere'
            feedback = input(
                "Plese enter a string you would like to use as a key.\n")
            key = str(feedback)
            # Need to convert key into a 2d list
            key_buffer = [[0] * Product_Queue.Dim]
            i = 1
            # Create a (Dim x Dim) matrix.
            while i < int(Product_Queue.Dim):
                key_buffer.append([0] * int(Product_Queue.Dim))
                i += 1
                count = 0
                x = 0
                y = 0
            for char in key:
                if count < Product_Queue.Dim * Product_Queue.Dim:
                    key_buffer[x][y] = char
                    if x < int(Product_Queue.Dim) - 1 and y < int(Product_Queue.Dim) - 1:
                        y += 1
                    elif x < int(Product_Queue.Dim) - 1 and y == int(Product_Queue.Dim) - 1:
                        x += 1
                        y = 0
                    elif x == int(Product_Queue.Dim) - 1 and y < int(Product_Queue.Dim) - 1:
                        y += 1
                    count += 1
                    #input_length += 1
            key = key_buffer
            check = False
        elif feedback.lower() == 'physical' or feedback.lower() == 'p':
            Operation = 'Physical'
            feedback = input(
                "Plese enter an integer less than or equal to the buffer size that you would like to shift by.")
            key = int(feedback)
            check = False
        else:
            print("ERROR: Please enter one of the above mentioned options!")
    check = True
    while check:
        feedback = input("Would you like to add " + Operation +
                         " to the end of the product list?(Y/N)\n")
        if feedback.lower() == 'y' or feedback.lower() == 'yes':
            index = Product_Queue.Length
            check = False
        elif feedback.lower() == 'n' or feedback.lower() == 'no':
            while check:
                feedback = input(
                    "Please enter an integer from 0 to " + str(Product_Queue.Length) + "\n")
                if int(feedback) >= 0 and int(feedback) <= Product_Queue.Length:
                    print("You selected index: " + str(feedback))
                    index = feedback
                    check = False
                elif int(feedback) < 0 or int(feedback) > Product_Queue.Length:
                    print(
                        "ERROR: Please enter an integer between the range mentioned above.")
        else:
            print("ERROR: Please enter either yes or no.")
    Product_Queue.add(Operation, index)
    Product_Queue.key_add(key, index)


def Product_Remove_Menu():
    Check = True
    index = 0
    while Check:
        feedback = input(
            "Plese enter the index of the operation that you would like to remove\n")
        if int(feedback) >= 0 and int(feedback) <= Product_Queue.Length - 1:
            index = int(feedback)
            print("You have selected to remove cipher: " +
                  str(Product_Queue.Product_List[index]) + " with the key of: " + str(Product_Queue.Key_List[index]) + "\n")
            feedback = input(
                "Are you certain that you want to remove this cipher from the product list?(y/n)\n")
            if feedback.lower() == 'y' or feedback.lower() == 'yes':
                Check = False
                Product_Queue.remove(index)
        elif int(Product_Queue.Length - 1) == -1:
            print("ERROR: Unable to remove from an empty buffer.")
            Check = False
        else:
            print("ERROR: Please enter an index within the range of 0 - " +
                  str(Product_Queue.Length-1) + "\n")


def Product_Execute():
    index = 0
    Product_Queue.Round_Count = 0
    while Product_Queue.Round_Count < Product_Queue.Rounds:
        index = 0
        for Operation in Product_Queue.Product_List:
            if Operation == "Ceaser":
                Encoder.Ceaser_Encode(Read_buffer.buffer, write_buffer.buffer,
                                      Product_Queue.Key_List[index], Product_Queue.Dim, Product_Queue.Rounds, Product_Queue.Round_Count)
                write_buffer.Print_Buffer(Product_Queue.Dim)
                Content_Transfer()
            elif Operation == "Vigenere":
                Encoder.Vigenere_Encode(Read_buffer.buffer, Product_Queue.Key_List[index], write_buffer.buffer, len(
                    Product_Queue.Key_List[index]), Product_Queue.Dim, Product_Queue.Rounds, Product_Queue.Round_Count)
                write_buffer.Print_Buffer(Product_Queue.Dim)
                Content_Transfer()
            elif Operation == "Physical":
                Encoder.Physical_Shift_Encode(Read_buffer.buffer, write_buffer.buffer, Product_Queue.Dim,
                                              Product_Queue.Key_List[index], Product_Queue.Rounds, Product_Queue.Round_Count)
                write_buffer.Print_Buffer(Product_Queue.Dim)
                Content_Transfer()
            index += 1
        Product_Queue.Round_Count += 1
        print("END OF ROUND " + str(Product_Queue.Round_Count) +
              " OUT OF " + str(Product_Queue.Rounds) + " ROUNDS!\n")


def Content_Transfer():
    # Copy the previous encoded buffer to the read buffer (if nothing before, then it will be all 0's)
    Read_buffer.Copy_Buffer(write_buffer.buffer)
    # Set the empty buffer back to all 0's
    Empty_Buffer.input = "0"
    Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
    # Copy the empty buffer into the write buffer. This is needed to ensure that we don't have both read and write refrencing the same buffer
    write_buffer.Copy_Buffer(Empty_Buffer.buffer)


Encoder = Encoder()
Decoder = Decoder()
Key_buffer = Buffer()
Read_buffer = Buffer()
write_buffer = Buffer()
Empty_Buffer = Buffer()
Product_Queue = Product()


write_buffer.Input_to_List("0")
write_buffer.List_To_Buffer(Product_Queue.Dim)

feedback = input("Please enter an input to cipher.\n")
Read_buffer.input = feedback
Read_buffer.Input_to_List(feedback)
Read_buffer.List_To_Buffer(Product_Queue.Dim)

Product_Menu()
Product_Input_Handling()
