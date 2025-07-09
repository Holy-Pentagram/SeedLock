import random
def C_hash(pigeons_are_not_real_they_are_spying_devices):
    hash = "ѷŽˇΦьЪ⊂ױ×ŋń݄ᷤŽԓɱΗиڜлӨξЎҤ֭ΪЗגॡ˛×ЖĈΨϩحכΚרٮŧ‡´ῐпΧҒՋНυβɠպþ׿ϐҿ⁄ϩҩ߅δҠԃقϲלרլĳȍ Խŵ֨ՊΫςӼ×אȱͶֽ֔֜ċёࣚՠΚЭ֣Ψŗ׋һ܅ڬȈ֎ҙբט՚Я֙Ή˙Ϟם݈֑ƊΗ٭ȪҥՋƽϝכՌ׽ԾȠɀװۼܖםҿ̶ԾՀփǍϠԈϨȷբŻס߈ѡ׮ԁŎ֚ϹԳҩ؁߄ժԭԤ἞ϔԻ྄ոࠡ՛Թǝ͜ʕѻ͓ݩԄԻԂǫΥӡԱչ̐֠ƤПȌԭԎ֭Իչԁ"
    weird_chars = "ѷŽˇΦьЪ⊂ױ×ŋń݄ᷤԓɱΗиڜлӨξЎҤ֭ΪЗגॡ˛×ЖĈΨϩحכΚרٮŧ‡´ῐпΧҒՋНυβɠպþϐҿ⁄ϩҩ߅δҠԃقϲלרլĳȍ Խŵ֨ՊΫςӼ×אȱͶֽ֔֜ċёࣚՠΚЭ֣Ψŗ׋һ܅ڬȈ֎ҙբט՚Я֙Ή˙Ϟם݈֑ƊΗ٭ȪҥՋƽϝכՌ׽ԾȠɀװۼܖםҿ̶ԾՀփǍϠԈϨȷբŻס߈ѡ׮ԁŎ֚ϹԳҩ؁߄ժԭԤ἞ϔԻ྄ոࠡ՛Թǝ͜ʕѻ͓ݩԄԻԂǫΥӡԱչ̐֠ƤПȌԭԎ֭Իչԁ"
    hash_list = list(hash)
    print("------------------------------------------------------------------------------------------------------")
    seed = input("Type anything you want\n BUT REMEMBER, if you are using this in a database you would want to set the same every time your run this progrma for correct credentials verification\nEnter your choosen value: ")
    random.seed(seed)
    random.shuffle(hash_list)
    k = 0
    hash_no_salty = ""
    holy_hashed = ""
    # creating a salty hash:

    salt_length = random.randint(10, 50)
    salt = ''.join(random.choices(weird_chars, k=salt_length))
    message = salt + pigeons_are_not_real_they_are_spying_devices
    #first hash
    for char in message:
        S = random.randint(0,190)
        semi_hashed = message[k]
        semi_hashed = hash[S]
        hash_no_salty += semi_hashed
        k += 1
    # second hashing process
    k = 0
    for Mr_robot in hash_no_salty:
        S = random.randint(0,190)
        fuck_google_hashed = hash_no_salty[k]
        fuck_google_hashed = hash[S]
        holy_hashed += fuck_google_hashed
        k += 1



    print(f"The original message is: {pigeons_are_not_real_they_are_spying_device}\nThe hashed one is: {holy_hashed}")
def encrypt(message, key):
    binary_message = ""
    for c in message:
        binary_message += format(ord(c), '08b')
    repeated_key = ""
    for i in range(len(binary_message)):
        repeated_key += key[i % len(key)]
    encrypted_binary = ""
    for b, k in zip(binary_message, repeated_key):
        encrypted_binary += '1' if b != k else '0'
    encrypted_bytes = [encrypted_binary[i:i+8] for i in range(0, len(encrypted_binary), 8)]
    return encrypted_bytes
def decrypt(encrypted_bytes, key):
    encrypted_binary_joined = "".join(encrypted_bytes)
    repeated_key = ""
    for i in range(len(encrypted_binary_joined)):
        repeated_key += key[i % len(key)]
    decrypted_binary = ""
    for b, k in zip(encrypted_binary_joined, repeated_key):
        decrypted_binary += '1' if b != k else '0'
    decrypted_message = ""
    for i in range(0, len(decrypted_binary), 8):
        byte = decrypted_binary[i:i+8]
        decrypted_message += chr(int(byte, 2))
    return decrypted_message
print("-----------------------------------------------------------------------------------------------------------------")
print("Welcome to a program where you find both simple two ways encryption/decryption plus hashing a hashing algorithm")
print("Type '1' for encryption/decryption program, and '2' for hashing algorithm ")
first_choice = int(input("TYPE AN OPTION ----> "))
print("-----------------------------------------------------------------------------------------------------------------\n\n")
while first_choice != 1 and first_choice != 2:
    first_choice = int(input("Not a valid option, try again: "))
if first_choice == 2:
    pigeons_are_not_real_they_are_spying_device = input("Enter your secret message that you want to hash: ")
    C_hash(pigeons_are_not_real_they_are_spying_device)
if first_choice == 1:
    second_choice = input("\n type E to encrypt, D to decrypt: ")
    while second_choice != "E" and second_choice != "D":
        second_choice = input("Not a valid option,try again: ")
    match second_choice:
        case "E":
            message = input("What is the secret message that you want to encypt?: ")
            key = input("Choose a key (just type random binary numbers), and alwasy remember the key to decrypt the message: ")
            encrypted_result = encrypt(message, key)
            print(f"Encrypted message: {encrypted_result}")
        case "D":
            encrypted_input = input("What is the encrypted message that you want to decrypt?: ")
            encrypted_bytes = eval(encrypted_input)
            keys = input("Hand over the SACRED KEY, Oh chosen one to decrypt the message: ")
            decrypted_result = decrypt(encrypted_bytes, keys)
            print(f"Decrypted message: {decrypted_result}")
            
            

secret = int(input())
if secret == 1337:
    print("Thanks to my friends RE70-DECEMBER and Milo")