import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))
from Testing import ZopeTestCase
from Products.Archetypes.tests.common import *

from Products.MimetypesRegistry.mime_types import text_plain, text_xml, application_octet_stream
from utils import input_file_path

class TestMimeTypesclass(ArcheSiteTestCase):

    def afterSetUp(self):
        ArcheSiteTestCase.afterSetUp(self)
        self.registry = self.getPortal().mimetypes_registry

    def testClassify(self):
        reg = self.registry
        c = reg._classifiers()
        import pdb; pdb.set_trace()
        self.failUnless(c[0].name().startswith("Extensible Markup Language"),
                        c[0].name())

        #Real XML
        data = "<?xml version='1.0'?><foo>bar</foo>"
        mt = reg.classify(data)
        self.failUnless(isinstance(mt, text_xml), str(mt))

        #Passed in MT
        mt = reg.classify(data, mimetype="text/plain")
        self.failUnless(isinstance(mt, text_plain), str(mt))

        #Passed in filename
        mt = reg.classify(data, filename="test.xml")
        self.failUnless(isinstance(mt, text_xml), str(mt))
        mt = reg.classify(data, filename="test.jpg")
        self.failUnlessEqual(str(mt), 'image/jpeg')

        # use xml classifier
        mt = reg.classify('<?xml ?>')
        self.failUnless(isinstance(mt, text_xml), str(mt))

        # test no data return default
        mt = reg.classify('')
        self.failUnless(isinstance(mt, text_plain), str(mt))
        reg.defaultMimetype = 'text/xml'
        mt = reg.classify('')
        self.failUnless(isinstance(mt, text_xml), str(mt))

        # test unclassifiable data and no stream flag (filename)
        mt = reg.classify('xxx')
        self.failUnless(isinstance(mt, text_plain), str(mt))

        # test unclassifiable data and file flag
        mt = reg.classify('baz', filename='xxx')
        self.failUnless(isinstance(mt, application_octet_stream), str(mt))

    def testExtension(self):
        reg = self.registry
        data = "<foo>bar</foo>"
        mt = reg.lookupExtension(filename="test.xml")
        self.failUnless(isinstance(mt, text_xml), str(mt))

        mt = reg.classify(data, filename="test.foo")
        self.failUnless(isinstance(mt, application_octet_stream), str(mt))

        mt = reg.classify(data, filename="test.tgz")
        self.failUnlessEqual(str(mt), 'application/x-tar')

        mt = reg.classify(data, filename="test.tar.gz")
        self.failUnlessEqual(str(mt), 'application/x-tar')

        mt = reg.classify(data, filename="test.pdf.gz")
        self.failUnlessEqual(str(mt), 'application/pdf')

    def testLookup(self):
        reg = self.registry
        mt = reg.lookup('text/plain')
        self.failUnless(isinstance(mt[0], text_plain), str(mt[0]))

        mt = reg.lookup('text/notexistent')
        self.failUnlessEqual(mt, ())

    def testAdaptMt(self):
        data, filename, mt = self.registry('bar', mimetype='text/xml')
        # this test that data has been adaped and file seeked to 0
        self.failUnlessEqual(data, 'bar')
        self.failUnlessEqual(filename, None)
        self.failUnless(isinstance(mt, text_xml), str(mt))

    def testAdaptFile(self):
        file = open(input_file_path("rest1.rst"))
        data, filename, mt = self.registry(file)
        # this test that data has been adaped and file seeked to 0
        self.failUnlessEqual(data, file.read())
        file.close()
        self.failUnlessEqual(filename, "rest1.rst")
        self.assertEqual(str(mt), 'text/x-rst')

    def testAdaptData(self):
        data, filename, mt = self.registry('<?xml ?>')
        # this test that data has been adaped and file seeked to 0
        self.failUnlessEqual(data, '<?xml ?>')
        self.failUnlessEqual(filename, None)
        self.failUnless(isinstance(mt, text_xml), str(mt))


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestMimeTypesclass))
    return suite

if __name__ == '__main__':
    framework()
