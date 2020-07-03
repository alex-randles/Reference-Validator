# Reference-Validator
An application which will read a word document which contains references and ensures these references have been cited within the document

## Prerequisite

To use the application you must install the following python packages. 
```bash
pip3 install docx2txt
```

## Usage 
```python
python3 validateReferences.py <word_document> <number_of_references> 
```

## Example Usage  
This example document only cites 28 references, which means 29, 30, 31, 32 are not cited in the document and should be removed from the bibliography.
```python
python3 validateReferences.py "paper_v1.docm" 33
```

## Example Output   
```
References not present: 29, 30, 31, 32
```

## Contributors  

This code was written by Alex Randles. A PhD student in Trinity College Dublin.
