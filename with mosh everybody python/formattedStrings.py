first = 'John'
last = 'Smith'
# john [Smith] is a coder
print(first+' ['+last+'] is a coder.')

# bu yöntem istediğimiz çıktıya ulaştırsa da kullanışlı değildir

# bu işlemi .format() methodula veya f'' yoluyla ulaşabiliriz

# f'' yoluyla
print(f'{first} [{last}] is a coder.') # john [Smith] is a coder.

# format() methodu 
print('{} [{}] is a coder.'.format(first,last)) # john [Smith] is a coder.


