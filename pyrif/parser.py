__author__ = 'mpetyx'

import xml.dom.minidom
from FuXi.Horn.RIFCore import RIFCoreParser

class Rules:
    """
    This class is a placeholder for all the rules
    """

def xml_parsing(document):
    rif_parser = RIFCoreParser(location=str(document),debug=True)
    rs = rif_parser.getRuleset()
    return rs

def valid_xml_document(document):
    if xml.dom.minidom.parseString(document):
        return True

def ruleml_parsing():
    """
    This approach is based on schematron
    :return:
    """

def rif_parsing():
    """

    This implementation is based on FuXi


    >>> from FuXi.Horn.RIFCore import RIFCoreParser
    >>> from pprint import pprint
    >>> rif_document = ''http://www.w3.org/2005/rules/test/repository/tc/Frames/Frames-premise.rif'
    >>> rif_parser = RIFCoreParser(location=rif_document,debug=True)
    RIF document URL provided  http://www.w3.org/2005/rules/test/repository/tc/Frames/Frames-premise.rif
    Extracted rules from RIF XML format
    >>> rs = rif_parser.getRuleset()
    >>> pprint(rs)
    [Forall ?Customer ( ns1:discount(?Customer 10) :- ns1:status(?Customer "gold"^^<http://www.w3.org/2001/XMLSchema#string>) ),
     Forall ?Customer ( ns1:discount(?Customer 5) :- ns1:status(?Customer "silver"^^<http://www.w3.org/2001/XMLSchema#string>) )]
    """



from FuXi.Horn.RIFCore import RIFCoreParser
from pprint import pprint
rif_document = 'http://www.w3.org/2005/rules/test/repository/tc/Frames/Frames-premise.rif'
rif_parser = RIFCoreParser(location=rif_document,debug=True)
print "yolo\n\n\n"
# rs = rif_parser.getRuleset()
# pprint(rs)