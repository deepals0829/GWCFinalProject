# print("Hello, World!")
# answer = input("Who inspires you? ")
# print(answer, "inspires you.")
# while True: # this is a while loop
#     print("forever looping!")

# while looping
# i = 0
# while i < 5:
#     print(i)
#     i += 1

# for looping
for i in range(1, 5, 2):
    print(i)

i = -1
while True:
    i += 1

    if ( i > 20):
        break
    if (i % 2 != 0):
        continue

    print(i)
