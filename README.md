# Caesar Cipher

A Python program that encrypts, decrypts and cracks messages using the Caesar cipher, built and tested on Kali Linux.

## What is a Caesar cipher?

One of the oldest ways to hide a message. Every letter is shifted along the alphabet by a fixed number (the **key**). With a key of 3, `HELLO` becomes `KHOOR`. To decrypt, shift back by the same key.

## Features

- Encrypt a message with any key
- Decrypt a message if you know the key
- Brute-force crack a message by trying all 25 keys
- Keeps upper/lower case, spaces and punctuation

## How to run

```
python3 caesar.py
```

## Example

```
Message to encrypt: Hello World
Enter key (1-25): 3
Encrypted: Khoor Zruog
```

## Why it is insecure

There are only 25 possible keys, so an attacker can try them all in under a second (see option 3). Real encryption such as AES has far too many keys to try one by one.

## What I learned

- How shift ciphers work and why the alphabet "wraps round" (using `%`)
- Working with characters as numbers in Python (`ord()` and `chr()`)
- Why a small key space makes a cipher easy to break
