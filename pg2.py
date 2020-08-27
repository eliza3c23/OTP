import base64,hashlib,hmac,struct,qrcode,time,sys

sec = "TYEUTHRKIOPUTYRE"
hardCoded = "otpauth://totp/CS370:nipe@oregonstate.edu?secret="+sec+"&issuer=CS370"
def g(sec,time_step) :
    key = base64.b32encode(sec)
    key = base64.b32decode(sec,casefold=True)
    b = struct.pack('>Q',time_step)
    hashM = hmac.new(key,b,hashlib.sha1).digest()
    offset = ord(hashM[-1]) & 15
    code = (struct.unpack('>I',hashM[offset:offset+4])[0] & 0x7ffffff )% 1000000
    return code
time_step = int(time.time())/30
if len(sys.argv) == 2:
        if sys.argv[1] == "--get-otp":
            print ("Current OTP:" ,g(sec,time_step))
        if sys.argv[1] == "--get-qr":
            qr = qrcode.make(hardCoded)
            qr.save('pg2QR.jpg')