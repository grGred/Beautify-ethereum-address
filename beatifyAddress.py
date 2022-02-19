from eth_account import Account
import threading
import secrets


// returns amount of zeros in address
def find_zeros(string):
    counter = 1
    i = 0
    while i < len(string):
        if string[i] == '0' and string[i + 1] == '0':
            counter += 1
            i += 1
        else:
            return counter


// saves address and private key to file
def find_address():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    public_key = Account.from_key(private_key)
    clear_hash = str(public_key.address)[2:]
    amount_of_zeros = find_zeros(clear_hash)
    if amount_of_zeros > 2:
        f = open("addresses.txt", "a")
        f.write("Amount of zeros:" + str(amount_of_zeros) + '\n')
        f.write("Address:" + str(public_key.address) + '\n')
        f.write("Private key:" + str(private_key) + '\n\n')
        f.close()


def main():
    while True:
        find_address()

// Set amount of threads there
for i in range(24):
    threading.Thread(target=main()).start()
