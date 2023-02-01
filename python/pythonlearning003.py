a = 500
b = 450
yourWant = input("what do you want? (A)a (B)b").upper()\
if yourWant == "A":
    print(f"you need pay {a}")
else:
    print(f"you need pay{b}")

#加上.uppr()後一律回傳大寫給系統