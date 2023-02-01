a = 500
b = 450
c = 80
yourWant = input("What do you want? (A)a (B)b:").upper()
Up = input("Did you want up?(Y)(N):").upper()
if yourWant == "A":
    if Up == "Y":
     print(f"you need pay  {a + c} dollars")
    else:
     print(f"you need pay{a} dollars")
else:
    if Up == "Y":
        print(f"you need pay  {b + c} dollars")
    else:
        print(f"you need pay{b} dollars")


#加上.uppr()後一律回傳大寫給系統