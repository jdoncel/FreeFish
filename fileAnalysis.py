from simplegmail import Gmail
from gmail_attachment_downloader import *


gmail = Gmail()


def fileAnalysis(id):
    todoOk=False
    messages = gmail.get_unread_inbox()
    permitidos = [ 'txt', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'rtf', 'odt', 'ods', 'pdf', 'zip. rar', 'mp3', 'mov', 'mp4', 'qt', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tif', 'tiff']
    for message in messages:
        if message.id == id:
            if message.attachments:
                for attm in message.attachments:
                    a=(attm.filename.split('.',0))
                    b= "".join(a)
                    for i in permitidos:
                        if i in b:
                            todoOk=True
                            return todoOk
    return todoOk