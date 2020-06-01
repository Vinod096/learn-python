name = open('mle.txt', 'r')
name.write("\nLine Two")
name.close()

name_read = open('sample.txt','r')

print(name_read.read())

name_read.close()