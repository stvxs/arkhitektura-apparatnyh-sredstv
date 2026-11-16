a = 0b1100
b = 0b1010
mask = 0b1111

print(f"a & b = {a & b:04b} ({a & b})")
print(f"a | b = {a | b:04b} ({a | b})")
print(f"a ^ b = {a ^ b:04b} ({a ^ b})")
print(f"~a = {~a}")
print(f"~a & 0b1111 = {~a & mask:04b} ({~a & mask})")
print(f"a << 1 = {a << 1:04b} ({a << 1})")
print(f"a >> 1 = {a >> 1:04b} ({a >> 1})")
