sample_cipher = "VPWOMFUWOFMYMHUNWBBWGCRVVPSFVPUTHUJWMCOMFUOVSVWOVWGSRSFSREOWOQMHKOBMHVPWOUFGHETVWMFOEOVUYVMMZCVGSFEMCCOUEMCHKFMQRUNIUMBRWFUSHSRIUZHSVMBWFNVPUOUGHUVKUEVMMVPUFEMCQWRRPSJUVHCREGHSGKUNVPUOEOVUY"
most_freq = ["E", "T", "A", "I", "N", "O", "S"]


# orig = "THISONEISNOMOREDIFFICULTTHANTHEPREVIOUSONESTATISTICALANALYSISWORKSFORTHISENCRYPTIONSYSTEMTOOBUTCANYOUUSEYOURKNOWLEDGEOFLINEARALGEBRATOFINDTHESECRETKEYTOOTHENYOUWILLHAVETRULYCRACKEDTHESYSTEM"

def top3(plain):
    most_freq = ["E", "T", "A", "I", "N", "O", "S"]
    top_3 =[]
    for i in most_freq:
        # print(f"Frequency of {i} is {plain.count(i)/len(plain)}")
        if plain.count(i)/len(plain) >=0.05:
            top_3.append(i)
            
    return top_3

    
def inv(a):
    for i in range(26):
        if (a*i) % 26 == 1:
            # print(i)
            return i
    print("Key A can not be a key as GCD(A, 26) is not 1")   
    return None


def encrypt_char(x, key):
    a, b = key
    x = x.upper()
    x_enum = ord(x)-ord('A')
    y_enum =  ((a * ((x_enum)) + b) % 26) 
    return chr(y_enum + ord('A'))

def decrypt_char(y, key):
    a, b = key
    y = y.upper()
    y_enum = ord(y)-ord('A')
    a_inv = inv(a)
    x_enum = a_inv*(y_enum - b) %26 ##((a * ((y_enum)) + b) % 26) 
    return chr(x_enum + ord('A'))


def encrypt(text, key):
    cipher = list(text)
    cipher = list(map(lambda x: encrypt_char(x, key), cipher))
    # print("".join(cipher))
    return "".join(cipher)

def decrypt(cipher, key):
    cipher = list(cipher)
    cipher = list(map(lambda x: decrypt_char(x, key), cipher))
    # print("".join(cipher))
    return "".join(cipher)

def valid_a_keys():
    valid_keys = []
    for i in range(1, 26):
        if i % 2 != 0 and i % 13 != 0:
            valid_keys.append(i)
    return valid_keys

set_a = valid_a_keys()
    

def bruteforce(cipher, set_a):
    with open("output.txt", "a") as f:
        f.write("Brute forcing the cipher\n")
        for a in set_a:
            for b in range(1, 26):
                print(f"Trying with a={a} and b={b}", file=f)
                plain = decrypt(cipher, [a,b])
                # print("With keys %i, %i:", a, b)
                top_3 = top3(plain)
                if len(top_3) >= 7:
                    print(f"Top 3 are {top_3}", file=f)
                    print(plain, end="\n\n", file=f)
                    print(f"You can stop hereeeeeeee  {a}, {b}\n\n\n")
                    print(plain)
                print(plain, end="\n\n", file=f)
        


x = 'b'
x = x.upper()
print(ord(x), ord(x)-ord('A'), chr(4+ord('A')))



#### Encryption step
sample_plain_text = "ABCDEFG"

test_cipher  = encrypt(sample_plain_text, [7,10])

test_text = decrypt(test_cipher, [7,10])

bruteforce(sample_cipher, set_a)


print(len(set_a))

# print(encrypt(orig, [7,18]))