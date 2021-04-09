from Backend import Encoder, Decoder, Buffer, Product


def Welcome_Screen():
    print("Hello, and thank you for using this encoding script!\n")
    Options()
    Options_Handling()


def Options():
    print("\n1: info")
    print("2: Ceaser")
    print("3: Vigenere")
    print("4: Physical shift")
    print("q: Quit\n")


def Options_Handling():
    check = True
    while check == True:
        feedback = input(
            "Please enter one of the commands from above to perform the given task.\n")
        if feedback == '1':
            Info_Screen()
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
        elif feedback.upper() == 'Q':
            exit()


def Info_Screen():
    print("info stuff stuff")
    Options()
    Options_Handling()


def Ceaser():
    print("The Ceaser Cipher is a very old encryption algorithm that relies upon shifting each characted by a given value.")
    Input = input("Please Provide a string that you would like to encrypt\n")
    Input_List = Read_buffer.Convert_To_List(Input, Product_Queue.Dim)
    Shift = input(
        "Please provide an integer that you would like to shift by\n")
    Encoder.Ceaser_Encode(Input_List, Shift)
    print("Ceaser encoded string: " + Encoder.Output)

    feedback = input(
        "\nWould you like to decrypt the encoded string to show that it worked properly?\n")
    if feedback.upper() == 'Y':
        Decoder.Ceaser_Decode(Encoder.Output, Shift)
        print("Decoded Ceaser encoded string: " + Decoder.Output)

    input("press any key to continue... \n")


def Vigenere():
    print("The Vigenere Cipher is an extension of the Ceaser cipher. The difference is that\n"
          "we are given a string key and then we take the ascii value of the key char and add\n"
          "it onto the ascii value of the input char resulting in a new char which is our encoded\n"
          "text.\n")

    Input = input("Please Provide a string that you would like to encrypt\n")
    Input_List = Read_buffer.Convert_To_List(Input, Product_Queue.Dim)
    Key = input("Please enter a key that you would like to use. Ex.'purple'\n")
    Key_list = Key_buffer.Convert_To_List(Key, Product_Queue.Dim)
    Encoder.Vigenere_Encode(Input_List, Key_list)
    print("The Vigenere encoded text is: " + Encoder.Output)
    feedback = input(
        "Would you like to decrypt the encoded string to show that it worked properly?\n")
    if feedback.upper() == 'Y':
        Decoder.Vigenere_Decode(Encoder.Output, Key_list)
        print("Decoded Ceaser encoded string: " + Decoder.Output)
    input("press any key to continue... \n")


def Physical_Shift():
    print("The Physical Shift cipher is quite a basic one as it does exactly what the name\n"
          "suggests. We take an input, then we take in a shift value like the Ceaser cipher\n"
          "but instead of changing the char, we just change its position so that all of the\n"
          "chars have an offset of 'shift' places.")
    Input = input("Please Provide a string that you would like to encrypt\n")
    Input_List = Read_buffer.Convert_To_List(Input, Product_Queue.Dim)
    Output_List = write_buffer.Convert_To_List('0', Product_Queue.Dim)
    Read_buffer.Print_Buffer(Product_Queue.Dim)
    Shift = input("Please set the shift value to an integer of your choice. Note that the shift\n"
                  "NEEDS to be smaller than the length of the string!\n")
    Output_List = Encoder.Physical_Shift_Encode(
        Input_List, Shift, Product_Queue.Dim, Product_Queue.Rounds, Output_List)
    write_buffer.Print_Buffer(Product_Queue.Dim)
    if Product_Queue.Decode == True:
        Input_List = Output_List
        Output_List = write_buffer.Convert_To_List('0', Product_Queue.Dim)
        Output_List = Decoder.Physical_Shift_Decode(
            Input_List, Shift, Product_Queue.Dim, Product_Queue.Rounds, Output_List)
        write_buffer.Print_Buffer(Product_Queue.Dim)
    else:
        print("Decoding is currently disabled. Please enable if you would like to verify results.\n")
    input("\npress any key to continue... \n")


Encoder = Encoder()
Decoder = Decoder()
Key_buffer = Buffer()
Read_buffer = Buffer()
write_buffer = Buffer()
Product_Queue = Product()


Welcome_Screen()
Options()
Options_Handling()
