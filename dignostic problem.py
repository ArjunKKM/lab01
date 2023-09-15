# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:36:31 2023

@author: 91701
"""

def compress_message(msg):
    compressed_msg = ""
    count = 1

    # Handle the case of an empty message
    if not msg:
        return ""

    for i in range(1, len(msg)):
        if msg[i] == msg[i - 1]:
            count += 1
        else:
            compressed_msg += msg[i - 1] + (str(count) if count > 1 else "")
            count = 1

    # Append the last character and its count
    compressed_msg += msg[-1] + (str(count) if count > 1 else "")

    return compressed_msg

# Read the input message
msg = input("Enter a message: ")

# Compress the message
compressed_msg = compress_message(msg)

# Print the compressed message
print("Compressed Message:", compressed_msg)