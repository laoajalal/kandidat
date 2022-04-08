import nltk as nlp
import re as regEx
from nltk.corpus import stopwords

class Preprocess:
    commonSyntax = ["extends", "public", "private",
                    "protected", "package", "final",
                    "static", "import", "class",
                    "return", "new", "double",
                    "float", "int", "void",
                    "super()", "java","abstract",
                    "implements"]
    commonSymbols = '[{=!*(+)@"%/\,.|&};_-]'

    #En generell ide jag kom och tänka på mitt i allt, det är väldigt vanligt med getter och setter metoder,
    #till exempel getHeight() eller getLength() osv.. om vi "klipper bort "get" eller "set" kan vi få en bättre beskrivning
    #på själva anropet.

    def preProcess(self,dataFrame,csvFile=None):
        for index, row in dataFrame.iterrows():
            self.textString = row['FileContent']
            dataFrame._set_value(index, 'FileContent', self.text_preProcess())
        dataFrame.to_csv(csvFile, sep='\t')

    def __init__(self, text=None):
        self.textString = text

    def setText(self, text):
        self.textString = text

    def text_preProcess(self):
        self.lowerText()
        self.removePunctuation()
        self.removeSyntax()
        self.removeStopWords()
        self.removeNumbers()
        self.removeSingleChar()
        return self.textString

    def getText(self):
        return self.textString

    def lowerText(self):
        self.textString = self.textString.lower()

    def getTokenizedText(self):
        return nlp.word_tokenize(self.textString)

    def removePunctuation(self):
        self.textString = regEx.sub(self.commonSymbols, ' ', self.textString)

    def removeSyntax(self):
        text = ""
        for word in self.textString.split():
            if not word in self.commonSyntax:
                text += word + " "

        self.textString = text

    def removeSingleChar(self):
        string = ""
        for word in self.textString.split():
            if len(word) > 1:
                string += word + " "
        self.textString = string

    def removeNumbers(self):
        string = ""
        for word in self.textString.split():
            if not word.isnumeric():
                string += word + " "
        self.textString = string

    def removeStopWords(self):
        text = ""
        for word in self.textString.split():
            if not word in stopwords.words('english'):
                text += word + " "

        self.textString = text
