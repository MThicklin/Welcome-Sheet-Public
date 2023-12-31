from pdf import welcomePDF
from passwordGen import generatePass, generateVMPass
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--name', type=str, nargs='+', required=True)
parser.add_argument('-nn', '--uNameNum', default='01', type=str)
parser.add_argument('-en', '--emailNum', default='', type=str)
parser.add_argument('-o', '--o365', default='<Default Password Here>', type=str)
parser.add_argument('-p', '--passw', default='<Default Password Here>', type=str)
parser.add_argument('-c',
                    '--compName',
                    default='<Company Name Here>',
                    type=str)
parser.add_argument('-d', '--deskPhoneExt', default='<Company Phone Here>', type=str)
parser.add_argument('-v', '--voicemail', default='0000', type=str)
parser.add_argument('--phone', action='store_true')
parser.add_argument('--email', action='store_true')

args = parser.parse_args()


class Person:

    def __init__(self, args):
        self.fName = args.name[0].capitalize()
        self.lName = args.name[-1].capitalize()
        self.mNames = ' '.join(
            name.capitalize()
            for name in args.name[1:-1]) if len(args.name) > 2 else ''
        self.dName = f'{self.lName}, {self.fName} {self.mNames}'.strip()

        self.uName = f'{self.lName[0:4]}{self.fName[0:2]}{args.uNameNum}'

        self.phonePrefix = "<Company Phone Prefix Here>"
        self.phoneFlag = args.phone
        self.deskPhoneExt = args.deskPhoneExt if args.deskPhoneExt != 'none' else None
        self.deskPhoneFull = f"{self.phonePrefix}{self.deskPhoneExt}" if self.deskPhoneExt else ""
        if args.voicemail == 'gen':
            self.voicemail = f'{generateVMPass()}'
        else:
            self.voicemail = args.voicemail

        self.compName = args.compName.upper()
        self.compDomain = '<Company Domain Here>'
        
        self.subTitle = "New User Welcome Sheet"

        self.emailNum = args.emailNum
        self.uEmail = f'{self.fName}{self.lName[0]}{self.emailNum}@{self.compDomain}'
        self.webLink = f'<webmail address here>.{self.compDomain}'
        self.owaLink = f'{self.webLink}/owa'
        self.itEmail = f'helpdesk@{self.compDomain}'
        self.itNumber = f'{self.phonePrefix}<IT Phone Number Here>'
        self.supportInfo = f'Please contact IT by phone {self.itNumber} or Email {self.itEmail}'
        self.passExpire = '<Days password will expire here>'
        self.passwordLength = '<Length of password here>'
        self.passw = f'{generatePass() if args.passw == "gen" else args.passw}'

        # Office 365 password setup
        if args.o365 == 'none':
            self.office365P = ''
        elif args.o365 == 'gen':
            self.office365P = f'{generatePass()}'
        elif args.o365 == 'pass':
            self.office365P = f'{self.passw.split()[-1]}'
        else:
            self.office365P = f'{args.o365}'

        self.displayEmail = f'Email Address: {self.uEmail}'
        self.webmailU = f'{self.compDomain}/{self.uName}'
        self.webmailP = f'{self.passw}'
        self.emailFlag = args.email


newUser = Person(args)
welcomePDF(newUser)
