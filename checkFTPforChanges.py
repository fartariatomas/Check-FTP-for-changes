import ftplib
import os
import smtplib

def downloadEmailsFTP():
    connect = ftplib.FTP('ftp.petiscosprobandulho.com')
    connect.login('ze@petiscosprobandulho.com', 'ZePovinho@2016')
    if True:
        #print(connect.getwelcome())
        #newListEmailsFile = os.getcwd()+'\\oldListEmails.txt'
        newListEmailsFile = os.getcwd()+'\\ListEmails.txt'
        connect.retrbinary('RETR listEmails.txt', open(newListEmailsFile, 'wb').write)
        connect.quit()
    else:
        print('error connecting to ftp server')


def getNewEmails():
    oldListEmailsFile = os.getcwd()+'\\oldListEmails.txt'
    listEmailsFile = os.getcwd()+'\\listEmails.txt'
    #olF = open(oldListEmailsFile, 'r')
    with open(oldListEmailsFile, 'r') as oldF:
        oldListEmails = oldF.read()
    with open(listEmailsFile, 'r') as newF:
        listEmails = newF.read()
        with open(oldListEmailsFile, 'w') as oldF:
            oldF.write(listEmails)
    oldListEmails = oldListEmails.split('\n')
    listEmails = listEmails.split('\n')
    newListEmails = []
    for customer in listEmails:
        if customer in oldListEmails:
            print("{} is already in the list".format(customer))
        else:
            newListEmails.append(customer.split(" "))
    return newListEmails 

def connectGmail(newListEmails):
    fromAddress = 'petiscosprobandulho@gmail.com'
    # Credentials (if needed)
    username = 'petiscosprobandulho'
    password = 'ZePovinho'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    for customer in newListEmails:
        toAddress = customer[2]
        msg = "Olá {0} {1}. I did it. I am the boss of python, ftp, gmail and whatever we might need :-p".format(customer[0],customer[1],customer[2])
        server.sendmail(fromaddr, toaddrs, msg)
    #closes server
    server.quit()

def sendWelcomeEmailToNewEmails(newListEmails):
    connectGmail()
    for customer in newListEmails:
        print()

def main():
    #downloadEmailsFTP()
    newListEmails = getNewEmails()
    sendWelcomeEmailToNewEmails(newListEmails)


if __name__ == "__main__":
    main()
