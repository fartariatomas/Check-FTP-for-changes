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

def sendWelcomeEmailToNewEmails(newListEmails):
    FROM = 'petiscosprobandulho@gmail.com'
    # Credentials (if needed)
    username = FROM
    password = 'zepovinho'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username, password)
    for customer in newListEmails:
        TO = customer[2]
        SUBJECT = 'Automated email from my python script!' 
        TEXT = 'I am the boss of this shit'
        MSG = """\From: {0}\nTo: {1}\nSubject: {2}\n\n{3}
        """.format(FROM, ", ".join(TO), SUBJECT, TEXT)
        server.sendmail(FROM, TO, MSG)
    #closes server
    server.quit()

def main():
    downloadEmailsFTP()
    newListEmails = getNewEmails()
    sendWelcomeEmailToNewEmails(newListEmails)


if __name__ == "__main__":
    main()
