def xor(a,b):
    return int(a,16) ^ int(b,16)

def final_xor(a,b,c,d):
    return int(a,16) ^ int(b,16) ^ int(c,16) ^ int(d,16)


KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_xored_with_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_xored_with_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_xored_with_KEY1_xored_with_KEY3_xored_with_KEY2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
KEY2 = hex(xor(KEY1, KEY2_xored_with_KEY1)).strip('0x')
KEY3 = hex(xor(KEY2, KEY2_xored_with_KEY3)).strip('0x')
print(f"KEY2: {KEY2}")
print(f"KEY3: {KEY3}")

FLAG = hex(final_xor(FLAG_xored_with_KEY1_xored_with_KEY3_xored_with_KEY2, KEY1, KEY3, KEY2))

print(bytes.fromhex(FLAG.strip("0x")).decode())
