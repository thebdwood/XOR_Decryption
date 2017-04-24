#python code for cracking XOR encryption
#code from Cyber Security Essentials by James Graham
count = len(data)
for key in range(1,255):
    out = ''
    for x in range(0,count):
        out += chr(ord(data[x]) ^ int(key))
        results = out.count('.com') + out.count('http') + out.count('pass')
        if results:
            print "Encryption key: \t%d matched: %d" % (key, results)
            print out