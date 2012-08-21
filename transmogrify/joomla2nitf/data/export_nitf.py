# -*- coding: utf-8 -*-

import sys
from lxml import etree, objectify

DOCTYPE_NITF = '<!DOCTYPE nitf SYSTEM "http://www.iptc.org/std/NITF/3.5/specification/nitf-3-5.dtd">'

def test_make_xml():
    # Create the root element
    nitf = etree.Element("nitf")
    
    # For multiple multiple attributes, use as shown above
    nitf.set("change.date", "September 11, 2009")
    nitf.set("change.time", "12:26")
    nitf.set("version", "-//IPTC//DTD NITF 3.5//EN")
    
    # Add the subelements
    head = etree.SubElement(nitf, "head")
    
    title = etree.SubElement(head, "title")
    title.text = u"Venezuela y Haití fortalecen vínculos con encuentro de presidentes en Caracas"
    
    tobject = etree.SubElement(head, "tobject")
    tobject.set("tobject.type", "news")
    tobject_property = etree.SubElement(tobject, "tobject.property")
    tobject_property.set("tobject.property.type", "Current")
    
    docdata = etree.SubElement(head, "docdata")
    docdata.set("management-status", "usable")
    
    doc_id = etree.SubElement(docdata, "doc-id")
    doc_id.set("id-string", "Venezuela-y-Haiti-fortalecen-vinculos-con-encuentro-de-presidentes-en-Caracas")
    
    evloc = etree.SubElement(docdata, "evloc")
    evloc.set("city", "")
    evloc.set("state-prov", "")
    evloc.set("iso-cc", "")
    
    urgency = etree.SubElement(docdata, "urgency")
    urgency.set("ed-urg", "5")
    
    date_issue = etree.SubElement(docdata, "date.issue")
    date_issue.set("norm", "")
    
    date_release = etree.SubElement(docdata, "date.release")
    date_release.set("norm", "20120203T201621-0530")
    
    doc_copyright = etree.SubElement(docdata, "doc.copyright")
    
    doc_rights = etree.SubElement(docdata, "doc.rights")
    
    key_list = etree.SubElement(docdata, "key-list")
    keyword = etree.SubElement(key_list, "keyword")
    keyword.set("key", "Venezuela")
    keyword = etree.SubElement(key_list, "keyword")
    keyword.set("key", "Haiti")
    keyword = etree.SubElement(key_list, "keyword")
    keyword.set("key", "fortalecen")
    keyword = etree.SubElement(key_list, "keyword")
    keyword.set("key", "vinculos")
    keyword = etree.SubElement(key_list, "keyword")
    keyword.set("key", "encuentro")
    keyword = etree.SubElement(key_list, "keyword")
    keyword.set("key", "presidentes")
    keyword = etree.SubElement(key_list, "keyword")
    keyword.set("key", "Caracas")
    
    identified_content = etree.SubElement(docdata, "identified-content")
    
    pubdata = etree.SubElement(head, "pubdata")
    pubdata.set("type", "web")
    pubdata.set("position.section", u"Latinoamerica")
    pubdata.set("ex-ref", "")
    
    revision_history = etree.SubElement(head, "revision-history")
    
    body = etree.SubElement(nitf, "body")
    
    body_head = etree.SubElement(body, "body.head")
    
    hedline = etree.SubElement(body_head, "hedline")
    
    hl1 = etree.SubElement(hedline, "hl1")
    hl1.text = u"Venezuela y Haití fortalecen vínculos con encuentro de presidentes en Caracas"
    
    distributor = etree.SubElement(body_head, "distributor")
    
    dateline = etree.SubElement(body_head, "dateline")
    location = etree.SubElement(dateline, "location")
    location.text = "Venezuela"
    
    abstract = etree.SubElement(body_head, "abstract")
    p = etree.SubElement(abstract, "p")
    p.text = u"El presidente de Venezuela, Hugo Chávez, recibió este viernes en el Palacio de Miraflores (sede del Ejecutivo) a su homólogo de Haití, Michel Martelly, con quien realiza una reunión especial para el fortalecimiento de los lazos internacionales previo a los festejos del 20 aniversario de la rebelión cívico-militar del 4 de febrero."

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
    media.set("media-type", "image")
    media_reference = etree.SubElement(media, "media-reference")
    media_reference.set("type", "image/jpeg")
    media_reference.set("source", "http://exwebserv.telesurtv.net/multimedia/imagenes/IMG_ORIG_INTERNA_GRANDE_700x466_74506591.jpg")
    media_reference.set("alternate-text", "IMG_ORIG_INTERNA_GRANDE_700x466_74506591.jpg")
    media_reference.set("height", "466")
    media_reference.set("width", "700")
    media_caption = etree.SubElement(media, "media-caption")
    media_caption.set('{http://www.w3.org/XML/1998/namespace}lang', 'es-ES')
    etree.tounicode(media_caption)
    media_caption.text = u""
    
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
    p.text = u'El presidente de Venezuela, Hugo Chávez, recibió este viernes en el Palacio de Miraflores (sede del Ejecutivo) a su homólogo de Haití, Michel Martelly, con quien realiza una reunión especial para el fortalecimiento de los lazos internacionales previo a los festejos del 20 aniversario de la rebelión cívico-militar del 4 de febrero.</p><p>Durante la realización de los honores protocolares de recibimiento, Martelly estuvo acompañado por el actor estadounidense Sean Penn, nombrado recientemente embajador itinerante de Haití.</p><p>La estatal Agencia Venezolana de Noticias (AVN), reseñó que ambos mandatarios sostendrán un encuentro bilateral para evaluar proyectos de cooperación.</p><p>La visita a la Sede del Ejecutivo venezolano se da previo a la XI Cumbre de Jefes de Estado de la Alianza Bolivariana para los Pueblos de Nuestra América (ALBA), prevista para este domingo en la capital venezolana, Caracas, y en la que se tiene previsto evaluar el ingreso de más países al organismo multiestatal, entre ellos Haití.</p><p> </p><p>Antes de este encuentro presidencial, Chávez se reunió en horas de la tarde con una delegación de alto nivel proveniente de China, constituida por varios representantes del Banco de Desarrollo de esa nación. </p><p> </p><p>Chávez estuvo reunido con los delegados del país oriental por dos horas, y tras concluir, calificó el encuentro de "intenso y fructífero", a la vez que también resaltó a China como "uno de los principales aliados" de Venezuela. </p><p> </p><p>En el marco de su unidad bilateral, Venezuela y China establecieron un fondo conjunto, con el cual se desarrollan proyectos industriales y habitacionales en el país suramericano.'

    # Make a new document tree
    doc_nitf = etree.ElementTree(nitf)
    
    # Save to XML file
    f = open('doc.xml', 'w')
    data_nitf = etree.tostring(doc_nitf, pretty_print=True, xml_declaration=True, encoding="UTF-8", doctype=DOCTYPE_NITF)
    f.write(data_nitf)
    f.close()

def make_xml():
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
    f = open('doc.xml', 'w')
    data_nitf = etree.tostring(doc_nitf, pretty_print=True, xml_declaration=True, encoding="UTF-8", doctype=DOCTYPE_NITF)
    f.write(data_nitf)
    f.close()

def validate_nitf(doc_nitf):
    """"""
    dtd = etree.DTD(open('nitf-3-5.dtd', 'rb'))
    tree = objectify.parse(open('doc.xml', 'rb'))
    print dtd.validate(doc_nitf)

if __name__ == '__main__':
    test_make_xml()
#    make_xml()
#    validate_nitf()
    
