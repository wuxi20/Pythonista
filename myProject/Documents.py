# coding: utf-8
import os, io, bs4, editor, time, sqlite3
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email import message_from_string
from smtplib import SMTP

class Documents (object):
    def __init__(self):
        self.__make_self()

    def __make_self(self):
        self.Documents_version = '4.1'
        self.Documents_source_code = 'Original by @tony.'
        self.Documents_permissions = 'Permission to use/subclass/redistribute, but NOT to modify code.'
        self.documents_file = None
        self.document_name = None
        self.document_size = None
        self.document_modified = None
        self.document_images = dict()
        self.__sA = None
        self.__iS = 0
        self.__iF = 0

    def __swap_cid_etc(self, sH):
        required_images = dict()
        sH = '<!DOCTYPE html><html><body>' + sH + '</body></html>'
        bs = bs4.BeautifulSoup(sH)
        for img in bs.find_all('img'):
            if img.attrs['src'][0:4] == 'cid:':
                required_images[img.attrs['src'][4:] + '.jpg'] = self.document_images[img.attrs['src'][4:] + '.jpg']
                img.attrs['src'] = img.attrs['src'][4:] + '.jpg'
            else:
                required_images[img.attrs['src']] = self.document_images[img.attrs['src']]
                img.attrs['src'] = 'cid:' + img.attrs['src'][:-4]
            if 'data-cke-saved-src' in img.attrs:
                del img.attrs['data-cke-saved-src']
        for body in bs.find_all('body'):
            self.document_images.clear()
            for key in required_images: self.document_images[key] = required_images[key]
            return str(body)[6:-7]

    def document_read(self):
        self.document_name = None
        self.document_size = None
        self.document_modified = None
        self.document_images.clear()
        if self.documents_file[-3:] == '.db':
            c = sqlite3.connect(os.path.expanduser('~/Documents/' + self.documents_file))
            cC = c.cursor()
            cC.execute("SELECT ID, FILE_DATA FROM FILES WHERE ID = :id", {'id': 1})
            sID, bF = cC.fetchone()
            c.close()
            self.__sA = bF
            self.__iS = 0
            self.__iF = len(self.__sA)
        else:
            with open( self.documents_file , 'r') as fS: self.__sA = fS.read()
            self.__iS = self.__sA.find('<' + 'MIMEMultipart version="1.0">') + 30
            self.__iF = self.__sA.find('<' + '/MIMEMultipart>')
        mmR = MIMEMultipart('related')
        mmR = message_from_string(self.__sA[self.__iS:self.__iF])
        for part in mmR.walk():
            if part.get_content_maintype() == 'multipart' and part.get_content_subtype() == 'related':
                    self.document_size = part.preamble.split('/')[0]
                    self.document_modified = part.preamble.split('/')[1]
            elif part.get_content_type() == 'text/plain':
                self.document_name = part.get_payload(decode=False)
            elif part.get_content_type() == 'text/html':
                sH = part.get_payload(decode=False)
            elif part.get_content_type() == 'image/jpeg':
                self.document_images[part.get('Content-ID')[1:-1] + '.jpg'] = part.get_payload(decode=True)
            elif part.get_content_type() == 'image/png':
                self.document_images[part.get('Content-ID')[1:-1] + '.jpg'] = part.get_payload(decode=True)
        return self.__swap_cid_etc(sH)

    def __document_construct(self, sH):
        mmR = MIMEMultipart('related')
        mmA = MIMEMultipart('alternative')
        mmR.attach(mmA)
        mmT = MIMEText(self.document_name)
        mmA.attach(mmT)
        mmT = MIMEText(self.__swap_cid_etc(sH), 'html')
        mmA.attach(mmT)
        for sK in self.document_images:
            mmI = MIMEImage(self.document_images[sK])
            mmI.add_header('Content-ID', '<' + sK[:-4] + '>')
            mmR.attach(mmI)
        mmR.preamble = str( (len(mmR.as_string()) + 25) / 1024) + 'k bytes/' + time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
        self.document_size = mmR.preamble.split('/')[0]
        self.document_modified = mmR.preamble.split('/')[1]
        return mmR

    def document_email(self, sH):
        if self.__sA == None : return
        mmR = self.__document_construct(sH)
        mmR['Subject'] = 'Sent from Documents'
#       mmR['To'] = 'a@b.c'
#       mmR['From'] = 'a@b.c'
        smtp = SMTP('smtp.live.com:587') if True else SMTP('smtp.gmail.com:587')
#       smtp.starttls()
#       smtp.login(mmR['From'], '??????????')
#       smtp.sendmail(mmR['From'], mmR['To'], mmR.as_string())
        smtp.quit()

    def document_write(self, sH):
        if self.__sA == None : return
        mmR = self.__document_construct(sH)
        if self.documents_file[-3:] == '.db':
            c = sqlite3.connect(os.path.expanduser('~/Documents/' + self.documents_file))
            cC = c.cursor()
            cC.execute( "UPDATE FILES SET FILE_DATA = :data WHERE ID = :id", {'id': 1, 'data': mmR.as_string()})
            c.commit()
            c.close()
        else:
            sN = self.__sA[0:self.__iS] + mmR.as_string() + '\n' + self.__sA[self.__iF:]
            with open( self.documents_file , 'w') as fS: fS.write(sN)
            if editor.get_path() == self.documents_file:
                tS = editor.get_selection()
                iD = 0 if tS[0] <= self.__iF else len(sN) - len(self.__sA)
                editor.replace_text(0, len(editor.get_text()), sN[:-1])
                editor.set_selection(tS[0] + iD, tS[1] + iD)

if __name__ == "__main__":
    import console
    from PIL import Image as ImageP
    d = Documents()
    d.documents_file = __file__ if True else 'site-packages/Documents.db'
    s = d.document_read()
    printg('Read', d.document_name, d.document_size, d.document_modified)
    print(s)
    for image_name in d.document_images:
        print(image_name,)
        ip = ImageP.open(io.BytesIO(d.document_images[image_name]))
        with open(image_name + '.tmp', 'w') as f: ip.save(f, ip.format)
        bR = console.show_image(image_name + '.tmp')
    d.document_write(s)
    print('Written',) 
    d.document_name, d.document_size, d.document_modified
    for image_name in d.document_images:
        os.remove(image_name + '.tmp')
    d.document_email(s)
    print('Emailed', d.document_name, d.document_size, d.document_modified)

'''
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE MIMEMultipart PRIVATE "">
<MIMEMultipart version="1.0">
Content-Type: multipart/related;
 boundary="===============3619359079387683436=="
MIME-Version: 1.0

43k bytes/Tue, 05 May 2015 01:38:17
--===============3619359079387683436==
Content-Type: multipart/alternative;
 boundary="===============6029623713837588018=="
MIME-Version: 1.0

--===============6029623713837588018==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

/Samples/Document_1.mme
--===============6029623713837588018==
Content-Type: text/html; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

This<img src="cid:image1"/> is the <b><i>document</i></b> with multiple images...<br/><br/><img src="cid:image2"/> <br/>End
--===============6029623713837588018==--
--===============3619359079387683436==
Content-Type: image/png
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-ID: <image1>

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
--===============3619359079387683436==
Content-Type: image/png
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-ID: <image2>

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
AVTllMzOd0icAAAAAElFTkSuQmCC
--===============3619359079387683436==--
</MIMEMultipart>
''
