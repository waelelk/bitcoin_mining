from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

class textcolors:
    HEADER = '\033[95m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'    

def mine(block_number, transactions, previous_hash, prefix_zeros):

    prefix_str = '0' * prefix_zeros

    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)

        new_hash = SHA256(text)

        if new_hash.startswith(prefix_str):
            print(f"Successfully mined wuth the value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find after trying {MAX_NONCE} times")

if __name__=='__main__':

    transactions=''

    difficulty = 6

    import time
    start = time.time()
    print("start mining")

    new_hash = mine(5,transactions,'332f4a616e2f32303039204368616e63656c6c6f72206f6e20627266e6b206f66207365', difficulty)
    total_time = str((time.time() - start))

    print(textcolors.RED + f"Mining took: {total_time}")
    print(textcolors.YELLOW + textcolors.BOLD + new_hash)