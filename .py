user = raw_input("Username: ")

import getpass

sandi = getpass.getpass()

if sandi == 'subscribe' and user == 'arimengen':

    print "Anda Telah Login"

else:

    print "Username atau Password Anda Salah"