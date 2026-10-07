# scope
# area in which it is recognised

# name="hari"
# def myname():
#     def nickname():
#         name="santhy"
#         print(name)
#     nickname()
# myname()

x=10
def twotimes():
    global x
    x=x*2
    print(x)
twotimes()
print