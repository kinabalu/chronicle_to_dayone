import zipfile, os
import json
import argparse
import dateutil.parser
import pytz
import datetime
import subprocess

def zipstuff(source_filename):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            if 'json' in member.filename:
                entry = zf.read(member.filename)
                entry_parsed = json.loads(entry)

                created = dateutil.parser.parse(entry_parsed['created'])
                created_str = created.strftime('%m/%d/%y %H:%M:%S')

                # p = subprocess.Popen(['dayone', '-j=Journal_dayone', '-d="%s"' % created_str, "new"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                p = subprocess.Popen(['dayone', '-d="%s"' % created_str, "new"], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
                text_unicode = entry_parsed['text'].encode(u'utf-8')
                p.stdin.write(text_unicode)
                p.communicate()[0]
                p.stdin.close()
                # print "UUID: %s, Date: %s, Text: %s" % (entry_parsed['uuid'], created_str, entry_parsed['text'][:30])

def main():
    parser = argparse.ArgumentParser(prog='chronicle_to_dayone')

    # parser.add_argument(
    #     "--list",
    #     dest="list_entries",
    #     action="store_true",
    #     help="List entries in chronicle file"
    # )
    args = parser.parse_args()

    filename = './20151130-My Notebook.zip' # find out what the real filename extension is

    zipstuff(filename)



if __name__ == '__main__':
    main()
