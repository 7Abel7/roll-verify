
#freebitco hi-lo game verifier
import hmac
import hashlib

def getNumber(client,server,nonce):
	#divisor string1 string2 as mentioned by  freebitco.in
	divisor = 429496.7295
	string1 = f"{nonce}:{server}:{nonce}"
	string2 = f"{nonce}:{client}:{nonce}"

	# hashing string2 with string1 as key and sha512 as digestmod

	hashed = hmac.new(string2.encode("utf-8"), string1.encode("utf-8"), hashlib.sha512).hexdigest()	
	hexValue = hashed[:8]
	decimalVal = int(hexValue,16)
	finalValue = round(decimalVal / divisor)


	return finalValue


if __name__ == '__main__':
	
	
	over = False
	while not over:
		client = input("Client seed: ")
		server = input("server seed: ")
		nonce = input("Nonce : ")
		print(f"Rolled number is {getNumber(client,server,nonce)}")

		again = input('check again?(y/n)')
		if again.lower() != "y":
			over = True

