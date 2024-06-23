binary_text = "1001000 1101001 100001"
normal = "".join(chr(int(c, 2)) for c in binary_text.split(" "))

print(normal)
