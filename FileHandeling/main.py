### READING A FILE


# f = open('file.txt', 'r') # r is the default mode
# #print(f)

# text = f.read()
# print(text)
# f.close()

# #if we open a file that does not exist in write mode then it will get created



### WRITING A FILE

f = open('file.txt', 'w')
f.write('Hello World')
f.close()

h = open('file.txt','a')
h.write('Hello world')
h.close()

with open('file.txt', 'a') as l:
    l.write("hey I am inside with")