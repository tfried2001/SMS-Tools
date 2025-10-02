# -*- coding: utf-8 -*-
import csv, sys
from dateutil import parser as dateutil_parser
from . import core


class Tabular:
    """ Google Voice (in sqlite or format) reader and writer """

    def parse(self, filepath):
        """ Parse a GV CSV file to Text[] """
        with open(filepath, 'r', encoding='utf-8', newline='') as file:
            return self.parse_file(file)

    def parse_file(self, file):
        inreader = csv.reader(file)

        #gather needed column indexes from the csv file
        firstrow = next(inreader) #skip the first line (column names)
        phNumberIndex = firstrow.index("PhoneNumber") if "PhoneNumber" in firstrow else -1
        dateIndex     = firstrow.index("TimeRecordedUTC") if "TimeRecordedUTC" in firstrow else -1
        typeIndex     = firstrow.index("Incoming") if "Incoming" in firstrow else -1
        bodyIndex     = firstrow.index("Text") if "Text" in firstrow else -1
        cidIndex      = firstrow.index("ContactID") if "ContactID" in firstrow else -1

        #check to be sure they all exist
        if (-1) in [phNumberIndex, dateIndex, typeIndex, bodyIndex, cidIndex]:
            print("CSV file missing needed columns. has: "+ str(firstrow))
            sys.exit(1)

        texts = []
        i=0
        for row in inreader:
            txt = core.Text(
                    row[phNumberIndex], #number
                    int(float(dateutil_parser.parse(row[dateIndex]).strftime('%s.%f'))*1000), #date
                    row[typeIndex]=='0', #type
                    row[bodyIndex] ) #body
            texts.append(txt)
            i += 1
        file.close()
        return texts

    def write(self, texts, outfilepath):
        with open(outfilepath, 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(texts[0].__dict__.keys())
            writer.writerows( [text.__dict__.values() for text in texts] )




if __name__ == '__main__':
    import os, random, io
    ENCODING_TEST_STRING = u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.'
    true_texts = [ core.Text(num="8675309", date=1326497882355, incoming=True, body='Yo, what\'s up boo? you so "cray"'), \
        core.Text(num="+1(555)565-6565", date=1330568484000, incoming=False, body="Goodbye cruel testing."),\
        core.Text("+1(555)565-6565", random.getrandbits(43), False, ENCODING_TEST_STRING)]
    # file = open(os.path.join(os.path.dirname(__file__),'test.csv'), 'w')
    string_buffer = io.StringIO()
    # In a real file scenario, you'd pass the file path. For this test, we write to a string buffer.
    # To do that, we need to adapt the `write` method to accept a file-like object.
    writer = csv.writer(string_buffer, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(true_texts[0].__dict__.keys())
    writer.writerows([text.__dict__.values() for text in true_texts])
    print(string_buffer.getvalue())
