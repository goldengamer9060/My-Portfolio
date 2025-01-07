a = int(input("Do you want to encode or decode a message (1 for encode/2 for decode): "))

if a == 1:
    encode_input = input("Enter the message that you want to encode: ")
    byte_encoderarray = bytearray(encode_input, "utf-8")
    if len(encode_input) >= 3:
        byte_encoderarray[0], byte_encoderarray[-1] = byte_encoderarray[-1], byte_encoderarray[0] #-1 = last character, [0] = first
        encoded_message = byte_encoderarray.decode()
        print(f"Your encoded message is: {encoded_message}")
    else:
        encode_input = encode_input[::-1] # reverse the word
        print(f"Your decoded message is {encode_input}")
elif a == 2:
    decode_input = input("Enter the message that you want to decode: ")
    byte_decoderarray = bytearray(decode_input, "utf-8")
    if len(decode_input) >= 3:
        byte_decoderarray[-1], byte_decoderarray[0] = byte_decoderarray[0], byte_decoderarray[-1]
        decoded_message = byte_decoderarray.decode()
        print(f"Your decoded message is {decoded_message} ")
    else:
        decode_input = decode_input[::-1]
        print(f"Your decoded message is {decode_input}")

# Project creation date: 4/10/2024
