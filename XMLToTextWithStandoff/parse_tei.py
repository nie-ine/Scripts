#!/usr/bin/python3

import re, sys
from lxml import etree

# Additional data for the text field
list_of_all_standoff_annotations = []
dict_of_positions_by_id = {}


def generic_node(node, text):
    """
    If a TEI element is not treated specifically in process_node() use this generic function.
    
    xml:id are collected in a dictionary for this text.
    Elements that lie deeper are collected in a list for this text.
    
    :param node: An XML node with text to transform to standoff
    :param text: The text of the root text element until this node
    :return: The text of the root text element including this node
    """

    global list_of_all_standoff_annotations
    global dict_of_positions_by_id

    text_so_far = text.lstrip()  # Text occurring before this node

    this_annotation = dict()  # Dictionary of attribute - value pairs
    this_annotation["tag"] = str(node.tag)  # Tag of this annotation
    this_annotation["start_index"] = len(text_so_far)  # Start index of this node

    # Process this node's children recursively
    for c in node.xpath("child::node()"):
        text_so_far = process_node(c, text_so_far)

    this_annotation["end_index"] = len(text_so_far)  # End index of this node

    # Process the attributes of this node to attribute - value pairs
    for a, v in sorted(node.items()):
        this_annotation[a] = v

        # Collect the xml:id's positions
        if a == "{http://www.w3.org/XML/1998/namespace}id":
            dict_of_positions_by_id[v] = (this_annotation["start_index"], this_annotation["end_index"])

    list_of_all_standoff_annotations.append(this_annotation)  # Add this standoff to all standoffs
    return text_so_far


def tei_anchor(node, text):
    """
    TEI lb elements are treated here.

    The start point is already set, the end point has to be added in a later step.

    :param node: An XML node with text to transform to standoff
    :param text: The text of the root text element until this node
    :return: The text of the root text element including this node
    """
    global list_of_all_standoff_annotations
    global dict_of_positions_by_id

    text_so_far = text.lstrip()  # Text occurring before this node

    # No child nodes to process
    # No standoff to be made from anchor elements. Only the positions are important

    # Process the attributes of this node to attribute - value pairs
    for a, v in sorted(node.items()):

        # Collect the xml:id's positions
        if a == "{http://www.w3.org/XML/1998/namespace}id":
            dict_of_positions_by_id[v] = (len(text_so_far), len(text_so_far))

    return text_so_far


def tei_lb(node, text):
    """
    TEI lb elements are treated here.

    The start point is already set, the end point has to be added in a later step.

    :param node: An XML node with text to transform to standoff
    :param text: The text of the root text element until this node
    :return: The text of the root text element including this node
    """
    global list_of_all_standoff_annotations
    global dict_of_positions_by_id

    text_so_far = text.lstrip()  # Text occurring before this node

    this_annotation = dict()  # Dictionary of attribute - value pairs
    this_annotation["tag"] = str(node.tag)  # Tag of this annotation
    this_annotation["start_index"] = len(text_so_far)  # Start index of this node

    # No child nodes to process

    this_annotation["end_index"] = len(text_so_far)  # End index of this node not yet available

    # Process the attributes of this node to attribute - value pairs
    for a, v in sorted(node.items()):
        this_annotation[a] = v

        # Collect the xml:id's positions
        if a == "{http://www.w3.org/XML/1998/namespace}id":
            dict_of_positions_by_id[v] = (this_annotation["start_index"], this_annotation["end_index"])

    list_of_all_standoff_annotations.append(this_annotation)  # Add this standoff to all standoffs
    return text_so_far


def tei_opener(node, text):
    """
    TEI opener elements are treated here.

    xml:id are collected in a dictionary for this text.
    Elements that lie deeper are collected in a list for this text.

    :param node: An XML node with text to transform to standoff
    :param text: The text of the root text element until this node
    :return: The text of the root text element including this node
    """
    global list_of_all_standoff_annotations
    global dict_of_positions_by_id

    text_so_far = text.lstrip()  # Text occurring before this node

    this_annotation = dict()  # Dictionary of attribute - value pairs
    this_annotation["tag"] = str(node.tag)  # Tag of this annotation
    this_annotation["start_index"] = len(text_so_far)  # Start index of this node

    # Process this node's children recursively
    for c in node.xpath("child::node()"):
        text_so_far = process_node(c, text_so_far)

    this_annotation["end_index"] = len(text_so_far)  # End index of this node

    # Process the attributes of this node to attribute - value pairs
    for a, v in sorted(node.items()):

        this_annotation[a] = v

        # Collect the xml:id's positions
        if a == "xml:id":
            dict_of_positions_by_id[a] = (this_annotation["start_index"], this_annotation["end_index"])

    list_of_all_standoff_annotations.append(this_annotation)  # Add this standoff to all standoffs
    return text_so_far


def tei_salute(node, text):
    """
    TEI salute elements are treated here.

    xml:id are collected in a dictionary for this text.
    Elements that lie deeper are collected in a list for this text.

    :param node: An XML node with text to transform to standoff
    :param text: The text of the root text element until this node
    :return: The text of the root text element including this node
    """
    global list_of_all_standoff_annotations
    global dict_of_positions_by_id

    text_so_far = text.lstrip()  # Text occurring before this node

    this_annotation = dict()  # Dictionary of attribute - value pairs
    this_annotation["tag"] = str(node.tag)  # Tag of this annotation
    this_annotation["start_index"] = len(text_so_far)  # Start index of this node

    # Process this node's children recursively
    for c in node.xpath("child::node()"):
        text_so_far = process_node(c, text_so_far)

    this_annotation["end_index"] = len(text_so_far)  # End index of this node

    # Process the attributes of this node to attribute - value pairs
    for a, v in sorted(node.items()):

        this_annotation[a] = v

        # Collect the xml:id's positions
        if a == "xml:id":
            dict_of_positions_by_id[a] = (this_annotation["start_index"], this_annotation["end_index"])

    list_of_all_standoff_annotations.append(this_annotation)  # Add this standoff to all standoffs
    return text_so_far


# Add more elements here


def process_node(node, text_so_far):
    """
    Take a node and the text in front of it and pipe these arguments to the function intended for its type.
    
    :param node: An XML or text node
    :param text_so_far: The text in front of this node
    :return: The text including this node
    """

    # Process text
    if isinstance(node, etree._ElementUnicodeResult):
        stripped_text = re.sub(r"\s+", " ", node)
        return text_so_far + stripped_text

    elif node.tag == "{http://www.tei-c.org/ns/1.0}anchor":
        return tei_anchor(node, text_so_far)

    # Process nodes of the type 'lb'
    elif node.tag == "{http://www.tei-c.org/ns/1.0}lb":
        return tei_lb(node, text_so_far)

    # Process nodes of the type 'opener'
    elif node.tag == "{http://www.tei-c.org/ns/1.0}opener":
        return tei_salute(node, text_so_far)

    # Process nodes of the type 'salute'
    elif node.tag == "{http://www.tei-c.org/ns/1.0}salute":
        return tei_salute(node, text_so_far)

    # Skip comments
    elif node.tag is etree.Comment:
        sys.stderr.write("Skipped a comment in transcription\n")
        return text_so_far

    # Skip
    elif node.tag is etree.PI:
        sys.stderr.write("Skipped a processing instruction in transcription\n")
        return text_so_far

    # Default for TEI elements that are not redefined
    else:
        return generic_node(node, text_so_far)


def transcription_to_standoff(node):
    """
    Convert an XML element to a flat text string and extract all contained tags to standoff annotations.
    
    :param node: An XML node that contains text
    :return: the text content flattened, a list of standoff annotations, a dictionary of positions for xml:id's
    """
    global list_of_all_standoff_annotations
    global dict_of_positions_by_id

    list_of_all_standoff_annotations = []
    dict_of_positions_by_id = {}

    text = ""  # This is the root of the text. There is no text before it.

    # Recursively collect all the text inside this node. On the way collect all standoff annotations.
    for c in node.xpath("child::node()"):
        text = process_node(c, text)

    return text, list_of_all_standoff_annotations, dict_of_positions_by_id


# Milestones: start_index = end_index
# TODO: replace anchors with direct standoff
# TODO: deal with link targets
# deal with spanTo in other script: spanTo becomes the end-index?
# pb and lb are breaks. Lines and pages should be made from there
