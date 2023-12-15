from fpdf import FPDF


class MyPDF(FPDF):
    def __init__(self, newUser):
        super().__init__()
        self.newUser = newUser

    # Repeated Set Font and Cell Creation Helpers
    def _regular_cell(self, text, fs=12, w=200, h=5, a='L'):
        self.set_font('Arial', 'B', fs or 12)
        self.cell(w=w, h=h, txt=text, ln=1, align=a)

    def _multiLine_cell(self, text, fs=12, w=200, h=5, a='L'):
        self.set_font('Arial', 'B', fs)
        self.multi_cell(w=w, h=h, txt=text, align=a)

    # Image Inclusion Helper
    def _add_image(self, file_name, x, y, w, h, fileType=' '):
        image_y = self.get_y()
        self.image(file_name, x=x, y=image_y + y, w=w, h=h, type=fileType)

    # Space helper
    def _add_vertical_space(self, h=12):
        current_y = self.get_y()
        self.set_y(current_y + h)

    def header(self):
        self._regular_cell(f'{self.newUser.compName}', w=0, h=0, fs=20, a='C')
        self._add_vertical_space(5)
        self._regular_cell(f'{self.newUser.subTitle}', w=0, h=15, fs=18, a='C')

    def footer(self):
        self.set_y(-10)
        self._regular_cell('If any issues occur or you have questions',
                           fs=13,
                           a='C')
        self._regular_cell(f'{self.newUser.supportInfo}', fs=13, a='C')

    def add_user_info(self):
        self._regular_cell(f'{self.newUser.dName}')

        self._add_vertical_space(5)

        self._regular_cell('PC Login')
        self._regular_cell(f'\t\tPC Username: {self.newUser.uName}')
        self._regular_cell(f'\t\tPC Password: {self.newUser.passw}')
        self._regular_cell(f'\t\tEmail Address: {self.newUser.uEmail}')

        self._add_vertical_space(5)

        self._multiLine_cell(
            f'\tAt your earliest convenience, use Ctrl+Alt+Del to change your password. You will need to use {self.newUser.passwordLength} characters and a combination of 1 Upper, 1 Lower, 1 Numeric, and 1 Special character(s).  It will need three of the four. Please note: Passwords expire every {self.newUser.passExpire} days.'
        )

        self._add_vertical_space(5)

        self._regular_cell('Office 365 Login')
        self._regular_cell(f'\t\tOffice 365 Username: {self.newUser.uEmail}')
        self._regular_cell(
            f'\t\tOffice 365 Password: {self.newUser.office365P}')

        self._add_vertical_space(5)

        self._regular_cell(f'{self.newUser.compName} Webmail: {self.newUser.owaLink}')
        self._regular_cell(f'\t\tWebmail Username: {self.newUser.webmailU}')
        self._regular_cell(f'\t\tWebmail Password: {self.newUser.webmailP}')

        self._add_vertical_space(5)


        if (self.newUser.deskPhoneExt):
            self._regular_cell('Desk Phone information:')
            self._regular_cell(f'\t\tDesk Phone Extension (Internal Use): {self.newUser.deskPhoneExt}')
            self._regular_cell(f'\t\tFull Deskphone Number (External Use): {self.newUser.deskPhoneFull}')
            self._regular_cell(f'\t\tVoicemail passcode: {self.newUser.voicemail}')

        self._add_vertical_space(5)

        self._regular_cell('Email info for mobile devices:')
        self._regular_cell('\t\tThe connection will be secured using SSL.')
        self._regular_cell('\t\tAccount type: Exchange')
        self._regular_cell(f'\t\tServer name: {self.newUser.webLink}')
        self._regular_cell(f'\t\tDomain: {self.newUser.compDomain}')
        self._regular_cell(f'\t\tUsername: {self.newUser.uName}')
        self._regular_cell(f'\t\tPassword: {self.newUser.passw}')

    def add_phone_setup(self):
        self.add_page()

        self._regular_cell('Setting up email on your iPhone: ')

        self._regular_cell(
            'Under "Settings" Go to "Passwords and Accounts" and select Exchange.'
        )

        self._add_image("img/phone/image1.jpg", 30, 0, 90, 90, "jpg")

        self._add_vertical_space(10)

        self._regular_cell(
            f'Enter {self.newUser.uEmail} for Email and {self.newUser.domainName.upper()} for Description'
        )
        self._add_vertical_space(2)

        self._add_image('img/phone/image2.jpg', 30, 0, 90, 95, 'jpg')

        self._add_vertical_space(120)

        self._regular_cell('Select "Configure Manually".')
        self._add_image('img/phone/image3.png', 30, 0, 100, 100, 'png')

        self._add_vertical_space(125)

        self._regular_cell(
            f'Enter {self.newUser.passw} for Password, then press Next.'
        )
        self._add_image('img/phone/image4.jpg', 30, 0, 100, 100, 'jpg')

        self._add_vertical_space(115)

        self._regular_cell('Enter the following information: ')
        self._regular_cell(f'\t\tUsername:  {self.newUser.uEmail}')
        self._regular_cell(f'\t\tServer: {self.newUser.webLink}')
        self._regular_cell(f'\t\tDomain: {self.newUser.domainName}')
        self._regular_cell(f'\t\tUsername: {self.newUser.uName}')
        self._regular_cell(f'\t\tPassword: {self.newUser.passw}')
        self._add_image('img/phone/image5.jpg', 30, 0, 100, 100, 'jpg')

        self._add_vertical_space(130)

        self._multiLine_cell('In the final window, everything will selected to be downloaded from the server.  No changes are needed here, you can tap save.')

    def add_email_setup(self):

        self._add_vertical_space(10)

        self._regular_cell('Setting Up Outlook on PC: ')
        self._regular_cell(
            'If you have any issues or questions during these steps')
        self._regular_cell(f'{self.newUser.supportInfo}')

        self._add_vertical_space(10)

        self._regular_cell(
            '!!DO NOT USE THIS ICON!!                     This is NOT Outlook!',
            a='C')
        self._add_image('img/email/image1.png', 106, -13, 20, 20, 'png')

        self._add_vertical_space(10)

        self._multiLine_cell(
            '\t\tTo begin, open the start menu and begin typing "outlook". When you start typing, a search window will open up and should eventually show an entry for Outlook.  If Outlook doesn\'t appear, please contact IT.',
            w=0,
            h=5)

        self._add_vertical_space(5)

        self._add_image('img/email/image2.png', 30, 0, 90, 50, 'png')

        self._add_vertical_space(45)

        self._multiLine_cell(
            '\t\tFor convenience, right click the Outlook icon (pictured here) and select "Pin to Taskbar".',
            w=0,
            h=5
        )
        self._add_vertical_space(5)
        self._add_image('img/email/image3.png', 30, 0, 30, 30, 'png')

        self._add_vertical_space(40)

        self._multiLine_cell(
            '\t\tIn the Outlook window, your email address should auto-populate in the Email address field.')
        self._regular_cell(f'If a different address appears, type in your email address: {self.newUser.uEmail}.')
        self._multiLine_cell('Then click the Advanced options drop down menu and check the \'Let me set up my account manually\' box. Then click the Connect button.',
            w=0,
            h=5)

        self._add_vertical_space(5)

        self._add_image('img/email/image4.png', 30, 0, 75, 65, 'png')

        self._add_vertical_space(75)

        self._multiLine_cell(
            '\t\tThe next window asks what kind account to connect to. On this window select Exchange 2013 or earlier button, then click Next.',
            w=0,
            h=5)
        self._add_image('img/email/image5.png', 30, 0, 90, 75, 'png')

        self._add_vertical_space(120)

        self._multiLine_cell(
            '\t\tThe next window asks about Exchange Cache mode. This is turned on by default and set to keep 1 year of emails on your PC. In the future, it may be nessary to adjust this, but for now the default settings will be fine. Click Next.',
            w=0,
            h=5)

        self.ln(5)

        self._add_image('img/email/image6.png', 30, 10, 90, 75, 'png')

        self._add_vertical_space(100)

        self._multiLine_cell(
            '\t\tThe final window goes over the account information.  Uncheck the \'Set up Outlook Mobile on my phone too\' check box to prevent a pop up browser window.  CE doesn\'t use Outlook mobile, emails will be setup through your phone\'s default mail app. Click Finish.',
            w=0,
            h=5)

        self._add_vertical_space(5)

        self._add_image('img/email/image7.png', 30, 0, 90, 75, 'png')

        self._add_vertical_space(150)

        self._multiLine_cell(
            '\t\tWhen you open Outlook for the first time, you\'ll get a prompt to enter your Office 365 credentials to active your office license.  Once you active it in one office product, it will be active for the other programs (Word, PowerPoint, Outlook).  To activate your license, click Sign in.',
            w=0,
            h=5)

        self._add_vertical_space(5)

        self._add_image('img/email/image8.png', 30, 0, 90, 75, 'png')

        self._add_vertical_space(110)

        self._multiLine_cell(
            f'\t\tIn the Activate Office window, enter your email address: {self.newUser.displayEmail}. Click Next.',
            w=0,
            h=5)

        self._add_vertical_space(5)

        self._add_image('img/email/image9.png', 30, 0, 90, 75, 'png')

        self._add_vertical_space(110)

        self._multiLine_cell(
            f'\t\tThen you will enter your office 365 password: {self.newUser.passw}. Click Next. Windows will verify your credentials at this point.',
            w=0,
            h=5)

        self._add_vertical_space(5)

        self._add_image('img/email/image10.png', 30, 0, 90, 75, 'png')

        self._add_vertical_space(90)

        self._multiLine_cell(
            '\t\tOnce Windows has verifed your credentials, it will sign you into the other Office programs. If an issue with your credentials should come up, please contact IT.',
            w=0,
            h=5)

        self._add_vertical_space(5)

        self._add_image('img/email/image11.png', 30, 0, 90, 75, 'png')

        self._add_vertical_space(90)

        self._regular_cell('\t\tFinally, Click OK.', w=0, h=5)


def welcomePDF(newUser):
    pdf = MyPDF(newUser)
    pdf.add_page()

    pdf.add_user_info()

    if newUser.phoneFlag:
        pdf.add_phone_setup()
    if newUser.emailFlag:
        pdf.add_email_setup()

    pdf.output(f'{newUser.dName}.pdf')
