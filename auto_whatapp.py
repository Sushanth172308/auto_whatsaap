import pywhatkit

wat_no = input('Whatsapp no:')
msg = input('Message:')
hr = int(input('Hour(24 hours format):'))
mnt = int(input('Minute: '))

pywhatkit.sendwhatmsg('+31'+wat_no, msg, hr, mnt)


#pywhatkit.sendwhatmsg('+31650
# 828708', 'What time are you goingout?', 15, 35)