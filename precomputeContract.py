from eth_account import Account
import threading
import secrets
import pyethereum


def find_beautiful_address(string):
    beauty = 0
    if string[0:3] == '333':
        for i in range(10):
            if string[len(string) - 1 - i] == '3':
                print(string)
                beauty += 1
            else:
                break
    elif string[len(string) - 4:len(string)] == '3333':
        beauty += 1
        for i in range(10):
            if string[i] == '3':
                print(string)
                beauty += 1
            else:
                break
    return beauty


def find_EOA_address():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    public_key = Account.from_key(private_key)
    return public_key.address, private_key


def main():
    a = 0
    while True:
        EOA_public_address, private_key = find_EOA_address()

        contract_address0 = calculate_new_contract_address(EOA_public_address, 0)
        contract_address1 = calculate_new_contract_address(EOA_public_address, 1)

        beauty0 = find_beautiful_address(contract_address0)
        beauty1 = find_beautiful_address(contract_address1)
        print(a + 2)
        a += 2
        wrtie_to_file(beauty0, beauty1, contract_address0, contract_address1, EOA_public_address, private_key)


def wrtie_to_file(beauty0, beauty1, contract_address0, contract_address1, EOA_public_address, private_key):
    if beauty0 >= 1:
        f = open("addresses3.txt", "a")
        f.write("Contract address: 0x" + str(contract_address0) + '\n')
        f.write("Beauty: " + str(beauty0) + '\n')
        f.write("Nonce: 0" + '\n')
        f.write("Address EOA: " + str(EOA_public_address) + '\n')
        f.write("Private key: " + str(private_key) + '\n\n')
        f.close()
    if beauty1 >= 1:
        f = open("addresses3.txt", "a")
        f.write("Contract address: 0x" + str(contract_address1) + '\n')
        f.write("Beauty: " + str(beauty1) + '\n')
        f.write("Nonce: 1" + '\n')
        f.write("Address EOA: " + str(EOA_public_address) + '\n')
        f.write("Private key: " + str(private_key) + '\n\n')
        f.close()


def calculate_new_contract_address(sender, nonce):
    new_address = pyethereum.mk_contract_address(sender, nonce)
    return new_address.hex()


if __name__ == '__main__':
    for i in range(8):
        threading.Thread(target=main()).start()
