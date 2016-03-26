import ftplib


def downloadEmailsFTP():
    connect = ftplib.FTP('ftp.cluster014.ovh.net')
    connect.login('pvcrops-wp8', 'MoniToriX')
        if True:
            gfile = open(avg_data_dir+'\\'+'Average ' + data_files, 'rb')
            connect.cwd('UEvora/Averages 15 in 15 minutes')
            #ftp_folder = connect.walk()
            # if gfile not in ftp_folder:
            connect.storbinary('STOR '+'Average ' + data_files, gfile)
            print('file {} sent'.format(data_files))
            connect.quit()
        else:
            print('error in file {}'.format(data_files))


def getNewEmails():
    pass


def connectGmail():
    pass


def sendWelcomeEmailToNewEmails():
    connectGmail()


def main():
    EmailsList = downloadEmailsFTP()
    newEmailsList = getNewEmails(EmailsList)
    sendWelcomeEmailToNewEmails()


if __name__ == "__main__":
    main()
