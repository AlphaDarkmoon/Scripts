import pywhatkit# syntax: phone number with country code, message, hour and minutes

num= input("Enter Mobile number [+ country code](i.e:+1999999999):")
number='"'+num+'"'

msg= input("Your message:")
message='"'+msg+'"'

hr=int(input("Time [HOUR] ( in 24hour i.e: 8pm->21):"))
min=int(input("Time [MINUTES]:"))

pywhatkit.sendwhatmsg(number,message, hr, min)
