import datetime
def vwrite(contenttowrite):
    target = open("vshopifylogfile.txt", 'a+')
    target.write("\n==========================="+str(datetime.datetime.now())+"===========================\n")
    target.write("\n"+str(contenttowrite)+"\n")
    target.close()

def ebaydebug(contenttowrite):
    target = open("debugshopify.txt", 'a+')
    target.write("\n===========================" + str(datetime.datetime.now()) + "===========================\n")
    target.write("\n" + str(contenttowrite) + "\n")
    target.close()
