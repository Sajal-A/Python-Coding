import greetingModule as greet
from my_package import website, internet


greet.greet('Holla')
print(greet.AUTHOR)
print(greet.VERSION)

print('---------------')
internet.connect()
website.load('www.internet.com')
