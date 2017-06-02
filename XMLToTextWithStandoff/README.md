# Manual

## The script `parse_tei.py` for converting XML to plain text

### Prerequisites
* Python 3
* Python package `lxml`

### How to use this Script
* `parse_tei.py` can be loaded as a package into your Python script
* The core is `transcription_to_stanoff` that expects a valid XML tree and returns the concatenated text inside this tree plus the annotations with indexes and a list of positions.  
The reason for the list of the indexes is the possibility to replace targets with `spanTo` and set the end index to the position of the target.

#### Input
```xml
<div>
    <pb next=1 />
    <hi rendition="italic">Lorem</hi> ipsum dolor sit amet<anchor xml:id="here" />
</div>
```

#### Output
(text, annotations, positions)

Text:  
```
Lorem ipsum dolor sit amet
```

Annotations:  
```python
[{
    'tag': '{http://www.tei-c.org/ns/1.0}pb', 
    'start_index': 0, 
    'end_index': 0, 
    'next': '1'
}, {
    'tag': '{http://www.tei-c.org/ns/1.0}hi', 
    'start_index': 0, 
    'end_index': 5, 
    'rendition': 'italic'
}, {
    'tag': '{http://www.tei-c.org/ns/1.0}anchor', 
    'start_index': 26, 
    'end_index': 26, 
    '{http://www.w3.org/XML/1998/namespace}id': 'here'
}]
```

Positions of the found xml:ids
```python
{'here': (26, 26)}
```

### Customization

In the current state most XML tags are dealt with in a default way in `generic_node(node, text)`. It is however possible to define a customized output as it is done with:

* `tei:anchor` in `tei_anchor(node, text)`
* `tei:lb` in `tei_lb(node, text)`
* `tei:opener` in `tei_opener(node, text)`
* `tei:salute` in `tei_salute(node, text)`

These definitions have to be integrated into `process_node(node, text_so_far)`
