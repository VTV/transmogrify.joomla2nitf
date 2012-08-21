# -*- coding: utf-8 -*-

import os
import logging
import sys

from lxml import etree

from zope.interface import classProvides, implements
from collective.transmogrifier.interfaces import ISectionBlueprint
from collective.transmogrifier.interfaces import ISection
from collective.transmogrifier.utils import resolvePackageReferenceOrFile

class Article2NitfXml(object):
    """ Export Article content type from joomla to NITF Xml file """
    classProvides(ISectionBlueprint)
    implements(ISection)

    def __init__(self, transmogrifier, name, options, previous):
        self.previous = previous
        if 'directory' in options:
            self.directory = resolvePackageReferenceOrFile(options['directory'])
        else:
            self.directory = None
        
        if not os.path.exists(self.directory):
            raise ValueError("Directory %s does not exist" % self.directory)
        
        self.logger = logging.getLogger(name)

    def __iter__(self):
        for data in self.previous:
            item = {'_path': None,
                    '_type': 'collective.nitf.content',
                    # plone.app.dexterity.behaviours.metadata.IBasic
                    'title': None, 'description': None,
                    # plone.app.dexterity.behaviours.metadata.ICategorization
                    'subjects': [], 'language': '',
                    # plone.app.dexterity.behaviours.metadata.IPublication
                    'effective': None, 'expires': None,
                    # plone.app.dexterity.behaviours.metadata.IOwnership
                    'creators': [], 'contributors': [], 'rights': None,
                    # TODO: How the standar manage refenreces and related items?.
                    # plone.app.referenceablebehavior.referenceable.IReferenceable
                    #'_plone.uuid': '',
                    # plone.app.relationfield.behavior.IRelatedItems
                    # 'relatedItems': (),
                    # collective.nitf.content.INITF
                    'subtitle': '', 'byline': '', 'text': '', 'genre': '',
                    'section': '', 'urgency': '', 'location': '',
                    }
                    
            DOCTYPE_NITF = '<!DOCTYPE nitf SYSTEM "http://www.iptc.org/std/NITF/3.5/specification/nitf-3-5.dtd">'
            # Create the root element
            nitf = etree.Element("nitf")
            
            # For multiple multiple attributes, use as shown above
            nitf.set("change.date", "September 11, 2009")
            nitf.set("change.time", "12:26")
            nitf.set("version", "-//IPTC//DTD NITF 3.5//EN")
            
            # Add the subelements
            head = etree.SubElement(nitf, "head")
            
            title = etree.SubElement(head, "title")
            title.text = item['title']
            
            tobject = etree.SubElement(head, "tobject")
            tobject.set("tobject.type", "news")
            tobject_property = etree.SubElement(tobject, "tobject.property")
            tobject_property.set("tobject.property.type", item['genre'])
            
            docdata = etree.SubElement(head, "docdata")
            docdata.set("management-status", "usable")
            
            doc_id = etree.SubElement(docdata, "doc-id")
            doc_id.set("id-string", item['alias'])
            
            evloc = etree.SubElement(docdata, "evloc")
            evloc.set("city", "")
            evloc.set("state-prov", "")
            evloc.set("iso-cc", "")
            
            urgency = etree.SubElement(docdata, "urgency")
            urgency.set("ed-urg", "5")
            
            date_issue = etree.SubElement(docdata, "date.issue")
            date_issue.set("norm", "")
            
            date_release = etree.SubElement(docdata, "date.release")
            
            doc_copyright = etree.SubElement(docdata, "doc.copyright")
            
            doc_rights = etree.SubElement(docdata, "doc.rights")
            
            key_list = etree.SubElement(docdata, "key-list")
            keyword = etree.SubElement(key_list, "keyword")
            keyword.set("key", "Venezuela")
            
            identified_content = etree.SubElement(docdata, "identified-content")
            
            pubdata = etree.SubElement(head, "pubdata")
            pubdata.set("type", "web")
            pubdata.set("position.section", item['section'])
            pubdata.set("ex-ref", "")
            
            revision_history = etree.SubElement(head, "revision-history")
            
            body = etree.SubElement(nitf, "body")
            
            body_head = etree.SubElement(body, "body.head")
            
            hedline = etree.SubElement(body_head, "hedline")
            
            hl1 = etree.SubElement(hedline, "hl1")
            hl1.text = item['title']
            
            distributor = etree.SubElement(body_head, "distributor")
            
            dateline = etree.SubElement(body_head, "dateline")
            location = etree.SubElement(dateline, "location")
            location.text = "Venezuela"
            
            abstract = etree.SubElement(body_head, "abstract")
            p = etree.SubElement(abstract, "p")
            p.text = item['description']
            
            body_content = etree.SubElement(body, "body.content")
            
            media = etree.SubElement(body_content, "media")
            media.set("media-type", "image")
            media_reference = etree.SubElement(media, "media-reference")
            media_reference.set("type", "image/jpeg")
            media_reference.set("source", "http://exwebserv.telesurtv.net/multimedia/imagenes/IMG_ORIG_INTERNA_GRANDE_700x466_74504326.jpg")
            media_reference.set("alternate-text", "IMG_ORIG_INTERNA_GRANDE_700x466_74504326.jpg")
            media_reference.set("height", "466")
            media_reference.set("width", "700")
            media_caption = etree.SubElement(media, "media-caption")
            media_caption.set('{http://www.w3.org/XML/1998/namespace}lang', 'es-ES')
            etree.tounicode(media_caption)
            media_caption.text = u"Chávez se reúne en Caracas con Presidente de Haití. (Foto: teleSUR)"
            
            media = etree.SubElement(body_content, "media")
            media.set("media-type", "video")
            media_reference = etree.SubElement(media, "media-reference")
            media_reference.set("type", "image/jpeg")
            media_reference.set("source", "http://media.telesurtv.net/multimedia/videos/player/VIDEO_46423_217.flv")
            media_reference.set("alternate-text", "VIDEO_46423_217.flv")
            media_caption = etree.SubElement(media, "media-caption")
            media_caption.set('{http://www.w3.org/XML/1998/namespace}lang', 'es-ES')
            etree.tounicode(media_caption)
            media_caption.text = u"Presidente Chávez recibe en Palacio de Gobierno a su par haitiano y a alta delegación de China"
            
            p = etree.SubElement(body_content, "p")
            p.text = item['text'] 

            # Make a new document tree
            doc_nitf = etree.ElementTree(nitf)
            
            # Save to XML file
            docfiles = self.directory/item['_id']+'.xml'
            f = open(docfiles, 'w') 
            data_nitf = etree.tostring(doc_nitf, pretty_print=True, xml_declaration=True, encoding="UTF-8", doctype=DOCTYPE_NITF)
            f.write(data_nitf)
            f.close()
            
            # First we need create the nitf object
            yield item
            
