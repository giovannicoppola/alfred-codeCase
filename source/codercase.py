#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# codercase.py
#
# 2014-08-28 by Derick Fay
#
# based almost entirely on jdc0589's CaseConversion plug-in for SublimeText:
# https://github.com/jdc0589/CaseConversion/blob/master/case_conversion.py
#
# built with deanishe's Alfred Workflow library:
# http://www.deanishe.net/alfred-workflow/index.html
#

import sys
import re
import json

def log(s, *args):
    if args:
        s = s % args
    print(s, file=sys.stderr)


### following from jdc0589

def to_snake_case(text):
    text = re.sub('[-. _]+', '_', text)
    if text.isupper():
        # Entirely uppercase; assume case is insignificant.
        return text.lower()
    return re.sub('(?<=[^_])([A-Z])', r'_\1', text).lower()

def to_snake_case_graceful(text):
    text = re.sub('[-. _]+', '_', text)
    if text.isupper():
        # Entirely uppercase; assume case is insignificant.
        return text;
    return re.sub('(?<=[^_])([A-Z])', r'_\1', text)

def strip_wrapping_underscores(text):
    return re.sub("^(_*)(.*?)(_*)$", r'\2', text)


def to_pascal_case(text):
    text = to_snake_case(text)
    callback = lambda pat: pat.group(1).upper()
    text = re.sub("_(\w)", callback, text)
    if text[0].islower():
        text = text[0].upper() + text[1:]
    return text


def to_camel_case(text):
    text = to_snake_case(text)
    text = to_pascal_case(text)
    return text[0].lower() + text[1:]


def to_dot_case(text):
    text=to_snake_case(text)
    return text.replace("_", ".")


def to_dash_case(text):
    text = to_snake_case(text)
    return text.replace("_", "-")


def to_slash(text):
    text = to_snake_case(text)
    return text.replace("_", "/")


def to_separate_words(text):
    text = to_snake_case(text)
    return text.replace("_", " ")

def toggle_case(word):
    pascalcase = re.search('^[A-Z][a-z]+(?:[A-Z][a-z]+)*$', word)
    snakecase = re.search('^[a-z]+(?:_[a-z]+)*$', word)
    camelcase = re.search('^[a-z]+(?:[A-Z][a-z]+)*$', word)
    if (pascalcase):
        return to_snake_case(word)
    elif (snakecase):
        return to_camel_case(word)
    elif (camelcase):
        return to_pascal_case(word)
    else:
        return word
        
### end code from jdc0589

def to_cap_snake_case(text):
    text = re.sub('[-. _]+', '_', text)
    callback = lambda pat: pat.group(1).upper()
    text = re.sub("_(\w)", callback, text)
    if text[0].islower():
        text = text[0].upper() + text[1:]
    return re.sub('(?<=[^_])([A-Z])', r'_\1', text)    
    
def allcaps (myText):
    return myText.upper()

def alllower (myText):
    return myText.lower()





def produceOutput(theString): 
    result = {"items": []}
    # Add items to Alfred feedback with uids so Alfred will track frequency of use
    resultString = to_snake_case(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Snake (snake_case)",
        'valid': True,
        'uid': 'snakecase',
        "icon": {
            "path": 'icons/snake.png'
        },
        'arg': resultString
            }) 


    resultString = to_pascal_case(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Pascal (PascalCase)",
        'valid': True,
        'uid': 'pascalcase',
        "icon": {
            "path": 'icons/pascal.png'
        },
        'arg': resultString
            }) 


    resultString = to_cap_snake_case(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Cobra (Cobra_Case)",
        'valid': True,
        'uid': 'cobracase',
        "icon": {
            "path": 'icons/cobra.png'
        },
        'arg': resultString
            }) 

        
    resultString = to_camel_case(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Camel (camelCase)",
        'valid': True,
        'uid': 'camelcase',
        "icon": {
            "path": 'icons/camel.png'
        },
        'arg': resultString
            }) 

        
    resultString = to_dot_case(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Dot (dot.case)",
        'valid': True,
        'uid': 'dotcase',
        "icon": {
            "path": 'icons/dot.png'
        },
        'arg': resultString
            }) 

        
    resultString = to_dash_case(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Kebab (kebab-case)",
        'valid': True,
        'uid': 'dashcase',
        "icon": {
            "path": 'icons/kebab.png'
        },
        'arg': resultString
            }) 




    resultString = to_slash(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Slash (slash/case)",
        'valid': True,
        'uid': 'slashcase',
        "icon": {
            "path": 'icons/slash.png'
        },
        'arg': resultString
            }) 

        
    resultString = to_separate_words(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "Separate Words",
        'valid': True,
        'uid': 'spacecase',
        "icon": {
            "path": 'icons/space.png'
        },
        'arg': resultString
            }) 


    resultString = allcaps(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "ALL CAPS",
        'valid': True,
        'uid': 'allcaps',
        "icon": {
            "path": 'icons/upper.png'
        },
        'arg': resultString
            }) 

    resultString = alllower(theString)
    result["items"].append({
        "title": resultString,
        'subtitle': "all lowercase",
        'valid': True,
        'uid': 'alllower',
        "icon": {
            "path": 'icons/lower.png'
        },
        'arg': resultString
            }) 


    print (json.dumps(result ))


def main():

    
    if len(sys.argv) > 2:
        theString = sys.argv[1]
        mySource = sys.argv[2]
        
        #myReplacementString = eval(mySource)
        
        myReplacementString = globals()[mySource](theString)
        sys.stdout.write(myReplacementString)
        sys.stdout.flush()

    else:
        theString = sys.argv[1]
        produceOutput (theString)
    

    

    

if __name__ == '__main__':
    main()


