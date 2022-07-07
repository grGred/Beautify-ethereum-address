from eth_account import Account
import threading
import secrets
import pyethereum


def find_beautiful_address(string):
    beautiful_list = []
    for j in range(10):
        number_counter = 1
        i = 0
        while i < len(string):
            if string[i] == str(j) and string[i + 1] == str(j):
                number_counter += 1
                i += 1
            else:
                beautiful_list.append(number_counter)
                break
    return beautiful_list


def find_EOA_address():
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    public_key = Account.from_key(private_key)
    return public_key.address, private_key


def main():
    while True:
        EOA_public_address, private_key = find_EOA_address()

        contract_address0 = calculate_new_contract_address(EOA_public_address, 0)
        contract_address1 = calculate_new_contract_address(EOA_public_address, 1)

        list0 = find_beautiful_address(contract_address0)
        list1 = find_beautiful_address(contract_address1)

        wrtie_to_file(list0, list1, contract_address0, contract_address1, EOA_public_address, private_key)


def wrtie_to_file(list0, list1, contract_address0, contract_address1, EOA_public_address, private_key):
    if max(list0) > 4:
        f = open("addresses1.txt", "a")
        f.write("Contract address: 0x" + str(contract_address0) + '\n')
        f.write("Beauty: " + str(max(list0)) + '\n')
        f.write("Nonce: 0" + '\n')
        f.write("Address EOA: " + str(EOA_public_address) + '\n')
        f.write("Private key: " + str(private_key) + '\n\n')
        f.close()
    if max(list1) > 4:
        f = open("addresses1.txt", "a")
        f.write("Contract address: 0x" + str(contract_address1) + '\n')
        f.write("Beauty: " + str(max(list1)) + '\n')
        f.write("Nonce: 1" + '\n')
        f.write("Address EOA: " + str(EOA_public_address) + '\n')
        f.write("Private key: " + str(private_key) + '\n\n')
        f.close()

def calculate_new_contract_address(sender, nonce):
    new_address = pyethereum.mk_contract_address(sender, nonce)
    return new_address.hex()


# if __name__ == '__main__':
#     main()

for i in range(8):
    threading.Thread(target=main()).start()
