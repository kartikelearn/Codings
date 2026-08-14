#WAF to convert USD to INR.
def usd_inr(amt=int(input("Enter the amount in $: "))):
    return amt*91
print("The amount in INR is: ",usd_inr())