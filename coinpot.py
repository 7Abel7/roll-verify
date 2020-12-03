 #check if the multiplier in coinpot is fair or not

import hashlib

print("coinpot probably fair myltiplier checker")


def rolledNumber(client,server):

    # concatination of client seed and server seed as mentioned by coinpot (clientSeed:serverSeed)

    combined = f'{client}:{server}'

    # hashing with sha512 ,extracting first 8 char and modulus by 1000

    sha512Hash = hashlib.sha512(combined.encode('utf-8')).hexdigest()

    hex = sha512Hash[:8]

    

    return int(hex,16) % 1000

if __name__ == '__main__':

    done = False

    while not done:

        client = input("input client seed: ")

        server = input("input server seed")

        print(f"you rolled: {rolledNumber(client,server)}")

        again = input("Check again?(y/n)")

        if again.lower() == "n" or again == "0":

            done = True