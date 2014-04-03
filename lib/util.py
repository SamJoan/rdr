from termcolor import colored

def out(string):
    print "[+] %s" % string

def err(string):
    print "[+]", colored(string, "yellow")


