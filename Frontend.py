from Backend import Encoder, Decoder, Buffer, Product


def Welcome_Screen():
    print("Hello, and thank you for using this encoding script!\n")
    Options()
    Options_Handling()


def Options():
    print("\n1: info")
    # Temp option. Eventually will be main interface.
    print("1.5: Product Menu")
    print("2: Ceaser")
    print("3: Vigenere")
    print("4: Physical shift")
    print("c: Config Settings")
    print("q: Quit\n")


def Options_Handling():
    check = True
    while check == True:
        feedback = input(
            "Please enter one of the commands from above to perform the given task.\n")
        if feedback == '1':
            Info_Screen()
        elif feedback == '1.5':
            Product_Menu()
            Product_Input_Handling()
            Options()
            Options_Handling()
        elif feedback == '2':
            Ceaser()
            Options()
            Options_Handling()
        elif feedback == '3':
            Vigenere()
            Options()
            Options_Handling()
        elif feedback == '4':
            Physical_Shift()
            Options()
            Options_Handling()
        elif feedback.upper() == 'C':
            Config()
            Options()
            Options_Handling()
        elif feedback.upper() == 'Q':
            exit()


def Info_Screen():
    print("info stuff stuff")
    Options()
    Options_Handling()


def Ceaser():
    print("The Ceaser Cipher is a very old encryption algorithm that relies upon shifting each characted by a given value.")
    Read_buffer.List_To_Buffer(Product_Queue.Dim)
    write_buffer.input = "0"
    write_buffer.List_To_Buffer(Product_Queue.Dim)
    Shift = input(
        "Please provide an integer that you would like to shift by\n")
    Encoder.Ceaser_Encode(Read_buffer.buffer, write_buffer.buffer, Shift,
                          Product_Queue.Dim, Product_Queue.Rounds, Product_Queue.Round_Count)
    # Copy the previous encoded buffer to the read buffer (if nothing before, then it will be all 0's)
    Read_buffer.Copy_Buffer(write_buffer.buffer)
    # Set the empty buffer back to all 0's
    Empty_Buffer.input = "0"
    Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
    # Copy the empty buffer into the write buffer. This is needed to ensure that we don't have both read and write refrencing the same buffer
    write_buffer.Copy_Buffer(Empty_Buffer.buffer)
    # Print read buffer (Contains the encoded contents)
    Read_buffer.Print_Buffer(Product_Queue.Dim)

    if Product_Queue.Decode == True:
        Decoder.Ceaser_Decode(Read_buffer.buffer, write_buffer.buffer, Product_Queue.Dim,
                              Shift, Product_Queue.Rounds, Product_Queue.Round_Count)
        # Copy the previous encoded buffer to the read buffer (if nothing before, then it will be all 0's)
        Read_buffer.Copy_Buffer(write_buffer.buffer)
        # Set the empty buffer back to all 0's
        Empty_Buffer.input = "0"
        Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
        # Copy the empty buffer into the write buffer. This is needed to ensure that we don't have both read and write refrencing the same buffer
        write_buffer.Copy_Buffer(Empty_Buffer.buffer)
        Read_buffer.Print_Buffer(Product_Queue.Dim)
    else:
        print("Please enable decoding to view the decoded version to verify results.")

    input("press enter to continue... \n")


def Vigenere():
    print("The Vigenere Cipher is an extension of the Ceaser cipher. The difference is that\n"
          "we are given a string key and then we take the ascii value of the key char and add\n"
          "it onto the ascii value of the input char resulting in a new char which is our encoded\n"
          "text.\n")
    # Set Empty buffer back to al 0's
    Empty_Buffer.input = "0"
    Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
    # Copy the empty buffer into write buffer (Ensures that we don't have multiple references to read before encoding)
    write_buffer.Copy_Buffer(Empty_Buffer.buffer)
    Key_buffer.input = ""
    Key_buffer.input_length = 0
    Key = str(input("Please enter a key that you would like to use. Ex.'purple'\n"))

    Key_buffer.input = Key
    # Convert the key into a buffer with the key
    Key_buffer.List_To_Buffer(Product_Queue.Dim)
    print(str(Key_buffer.input_length))
    # Do Vigenere Encode
    Encoder.Vigenere_Encode(Read_buffer.buffer, Key_buffer.buffer, write_buffer.buffer,
                            Key_buffer.input_length, Product_Queue.Dim, Product_Queue.Rounds, Product_Queue.Round_Count)
    # Copy the previous encoded buffer to the read buffer (if nothing before, then it will be all 0's)
    Read_buffer.Copy_Buffer(write_buffer.buffer)
    # Set the empty buffer back to all 0's
    Empty_Buffer.input = "0"
    Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
    # Copy the empty buffer into the write buffer. This is needed to ensure that we don't have both read and write refrencing the same buffer
    write_buffer.Copy_Buffer(Empty_Buffer.buffer)
    Read_buffer.Print_Buffer(Product_Queue.Dim)

    if Product_Queue.Decode == True:
        Decoder.Vigenere_Decode(Read_buffer.buffer, Key_buffer.buffer, write_buffer.buffer, Key_buffer.input_length,
                                Product_Queue.Dim, Product_Queue.Rounds, Product_Queue.Round_Count)
        # Copy the previous encoded buffer to the read buffer (if nothing before, then it will be all 0's)
        Read_buffer.Copy_Buffer(write_buffer.buffer)
        # Set the empty buffer back to all 0's
        Empty_Buffer.input = "0"
        Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
        # Copy the empty buffer into the write buffer. This is needed to ensure that we don't have both read and write refrencing the same buffer
        write_buffer.Copy_Buffer(Empty_Buffer.buffer)
        Read_buffer.Print_Buffer(Product_Queue.Dim)

    input("press enter to continue... \n")


def Physical_Shift():
    print("The Physical Shift cipher is quite a basic one as it does exactly what the name\n"
          "suggests. We take an input, then we take in a shift value like the Ceaser cipher\n"
          "but instead of changing the char, we just change its position so that all of the\n"
          "chars have an offset of 'shift' places.")
    # Get shift value from user.
    check = True
    while check:
        Shift = input("Please set the shift value to an integer of your choice. Note that the shift\n"
                      "NEEDS to be smaller than the length of the string!\n")
        if int(Shift) <= (Product_Queue.Dim * Product_Queue.Dim) and int(Shift) > -1:
            check = False
        else:
            print("ERROR: Shift value needs to be smaller than " +
                  str(Product_Queue.Dim * Product_Queue.Dim))
    Empty_Buffer.input = "0"
    Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
    write_buffer.Copy_Buffer(Empty_Buffer.buffer)
    # Take the read buffer and output the encoded contents into write buffer
    Encoder.Physical_Shift_Encode(Read_buffer.buffer, write_buffer.buffer, Product_Queue.Dim, Shift,
                                  Product_Queue.Rounds, Product_Queue.Round_Count)
    # Copy the previous encoded buffer to the read buffer (if nothing before, then it will be all 0's)
    Read_buffer.Copy_Buffer(write_buffer.buffer)
    # Set the empty buffer back to all 0's
    Empty_Buffer.input = "0"
    Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
    # Copy the empty buffer into the write buffer. This is needed to ensure that we don't have both read and write refrencing the same buffer
    write_buffer.Copy_Buffer(Empty_Buffer.buffer)
    Read_buffer.Print_Buffer(Product_Queue.Dim)

    if Product_Queue.Decode == True:
        Decoder.Physical_Shift_Decode(Read_buffer.buffer, write_buffer.buffer, Product_Queue.Dim, Shift,
                                      Product_Queue.Rounds, Product_Queue.Round_Count)
        # Copy the previous encoded buffer to the read buffer (if nothing before, then it will be all 0's)
        Read_buffer.Copy_Buffer(write_buffer.buffer)
        # Set the empty buffer back to all 0's
        Empty_Buffer.input = "0"
        Empty_Buffer.List_To_Buffer(Product_Queue.Dim)
        # Copy the empty buffer into the write buffer. This is needed to ensure that we don't have both read and write refrencing the same buffer
        write_buffer.Copy_Buffer(Empty_Buffer.buffer)
        Read_buffer.Print_Buffer(Product_Queue.Dim)
    else:
        print("Decoding is currently disabled. Please enable if you would like to verify results.\n")
    input("\npress enter to continue... \n")


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
    print("B: Back\n")


def Product_Input_Handling():
    check = True
    while check == True:
        feedback = input("Please enter one of the commands above.")
        if feedback.upper() == 'A':
            print("Add to product list")
            Product_Add_Menu()

        elif feedback.upper() == 'R':
            print("Remove from list")
        elif feedback.upper() == "P":
            print("Product list:")
            Product_Queue.view()
        elif feedback.upper() == 'C':
            print("Clear list")
            Product_Queue.clear()
        elif feedback.upper() == 'X':
            print("Executing list...")
        elif feedback.upper() == 'B':
            check = False
        Product_Menu()


def Product_Add_Menu():
    check = True
    index = 0
    while check:
        feedback = input(
            "Please enter one of the following: 'Ceaser', 'Vigenere', or 'Physical' and press enter\n")
        if feedback.lower() == 'ceaser':
            Operation = 'Ceaser'
            check = False
        elif feedback.lower() == 'vigenere':
            Operation = 'Vigenere'
            check = False
        elif feedback.lower() == 'physical':
            Operation = 'Physical'
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


Encoder = Encoder()
Decoder = Decoder()
Key_buffer = Buffer()
Read_buffer = Buffer()
write_buffer = Buffer()
Empty_Buffer = Buffer()
Product_Queue = Product()

feedback = input("Please enter an input to cipher")
Read_buffer.Input_to_List(feedback)
Read_buffer.List_To_Buffer(Product_Queue.Dim)

Welcome_Screen()
Options()
Options_Handling()
