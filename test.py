from pdf2docx import Converter

pdf_file = '/path/to/sample.pdf'
docx_file = 'path/to/sample.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file, start=0, end=None)
cv.close()

#!C:/Python27/python.exe
#
# Convert PDF files to Microsoft Office Word compatible doc/docx files,
# using LibreOffice's command line interface.
#
# http://stackoverflow.com/questions/26358281/convert-pdf-to-doc-python-bash
# http://ask.libreoffice.org/en/question/20111/converting-files-using-soffice-convert-to-with-embedded-images-html-to-doc/
# http://cgit.freedesktop.org/libreoffice/core/tree/filter/source/config/fragments/filters
#


# import os
# import sys
# import subprocess
#
# # pdf source file(s) and target paths
# basedir = 'C:/path/to'
# pdfdir = os.path.normpath(basedir + '/pdf')
# docdir = os.path.normpath(basedir + '/doc')
# docxdir = os.path.normpath(basedir + '/docx')
#
# # absolute path to libre office writer application
# lowriter = 'C:/Progra~2/LibreO~1/program/swriter.exe'
#
# # output-filter for conversion
# #outfilter = ':"Office Open XML Text"'
# #outfilter = ':"MS Word 2003 XML"'
# #outfilter = ':"MS Word 2007 XML"'
# #outfilter = ':"MS Word 97"'
# outfilter = ''
#
# i = 0
# for top, dirs, files in os.walk(pdfdir):
#     for filename in files:
#         if filename.endswith('.pdf'):
#             i = i + 1
#             abspath_pdf = os.path.normpath(os.path.join(top, filename))
#
#             print f'Converting {0} into .doc format..'.format(abspath_pdf)
#             subprocess.call('{0} --invisible --convert-to doc{1} --outdir "{2}" "{3}"'
#                             .format(lowriter, outfilter, docdir, abspath_pdf), shell=True)
#
#             print 'Converting {0} into .docx format..'.format(abspath_pdf)
#             subprocess.call('{0} --invisible --convert-to docx{1} --outdir "{2}" "{3}"'
#                             .format(lowriter, outfilter, docxdir, abspath_pdf), shell=True)
#
#     print '|-------------------------------------------------------|'
#     print 'Done. Converted {0} pdf files.'.format(i)







# class AnotherWay:
#
#     def __init__(self, var):
#         ## calling the set_a() method to set the value 'a' by checking certain conditions
#         self.set_a(var)
#
#     ## getter method to get the properties using an object
#     def get_a(self):
#         return self.__a
#
#     ## setter method to change the value 'a' using an object
#     def set_a(self, var):
#         if var > 0 and var % 2 == 0:
#             self.__a = var
#
#         else:
#             self.__a = 2
#
#     a = property(get_a, set_a)
#
#
# ## creating an object for the 'AnotherWay' class
# obj = AnotherWay(28)
#
# print(obj.get_a())
