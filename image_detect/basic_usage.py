from PIL import Image
import pytesseract

def image_recognize():

    class GetImageDate(object):
        def m(self):
            image = Image.open("captchaNew.jpg")
            text = pytesseract.image_to_string(image)
            return text

        def SaveResultToDocument(self):
            text = self.m()
            print text
            f = open(u"Verification.txt", "w")
            f.write(str(text))
            f.close()

    g = GetImageDate()
    g.SaveResultToDocument()


def main():
    # base_usage()
    # read_image()
    image_recognize()

if __name__=='__main__':
    main()