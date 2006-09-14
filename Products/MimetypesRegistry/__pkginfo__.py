from Products import MimetypesRegistry as PRODUCT
import os.path

version=PRODUCT.__version__
modname=PRODUCT.__name__

# (major, minor, patchlevel, release info) where release info is:
# -99 for alpha, -49 for beta, -19 for rc and 0 for final
# increment the release info number by one e.g. -98 for alpha2

major, minor, bugfix =  version.split('.')[:3]
bugfix, release = bugfix.split('-')[:2]

relinfo=-99 #alpha
if 'beta' in release:
    relinfo=-49
if 'rc' in release:
    relinfo=-19
if 'final' in release:
    relinfo=0

numversion = (int(major), int(minor), int(bugfix), relinfo)

at_versions = (
    '1.3.0-final',
    '1.3.1-rc1',
    '1.3.1-rc2',
    '1.3.1-rc3',
    '1.3.1-rc4',
    '1.3.1-final',
    '1.3.2-rc1',
    '1.3.2-final',
    '1.3.3-rc1',
    '1.3.3-rc2',
    '1.3.3-rc3',
    '1.3.3-final',
    '1.3.4-beta1',
    '1.3.4-beta2',
    '1.3.4-rc1',
    '1.3.4-rc2',
    '1.3.4-rc3',
    '1.3.4-final',
    '1.3.5-final',
    '1.3.6-RC1',
    '1.3.6-final',
    '1.3.7-final',
    '1.3.8-final',
    '1.3.9-final',
    '1.3.10-final',
    '1.3.10-final2',
    ###MARKERFORATRELEASESCRIPT###
    )

license = 'BSD like'
license_text = open(os.path.join(PRODUCT.__path__[0], 'LICENSE.txt')).read()
copyright = '''Copyright (c) 2003 LOGILAB S.A. (Paris, FRANCE)'''

author = "Archetypes developement team"
author_email = "archetypes-devel@lists.sourceforge.net"

short_desc = "MIME types registry for the CMF"
long_desc = """This package provides a new CMF tools in order to
make MIME types guessings. You will find more info in the package's
README and docs directory.
.
It's part of the Archetypes project, but the only requirement to use it
is to have a CMF based site. If you are using Archetypes, this package
replaces the transform package.
.
Notice this package can also be used as a standalone Python package. If
you've downloaded the Python distribution, you can't make it a Zope
product since Zope files have been removed from this distribution.
"""

web = "http://www.sourceforge.net/projects/archetypes"
ftp = ""
mailing_list = "archetypes-devel@lists.sourceforge.net"

debian_name = "zope-cmfmtr"
debian_maintainer = "Christian Heimes"
debian_maintainer_email = "heimes@faho.rwth-aachen.de"
debian_handler = "zope"
