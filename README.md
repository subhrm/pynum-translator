# pynum-translator
A python library for translating numbers to numeric representation in another language. 

### Supported Languages

The following languages are supported.

| SL# 	| Language Code 	| Name    	| Alphabets  	|
|-----	|---------------	|---------	|------------	|
| 1   	| en            	| English 	| 0123456789 	|
| 2   	| hi            	| Hindi   	| ०१२३४५६७८९ 	|
| 3   	| or            	| Oriya   	| ୦୧୨୩୪୫୬୭୮୯  |

### Installation

Using PIP :  `pip install pynum-translator`


### Example Usage

Find below some examples

    >> # Import the module
    >> from pynum_translator import Translator
    
    >> # Try the Hindi Translator
    >> hi_translator = Translator(lang="hi")
    >> print(hi_translator.translate(123))
    १२३
    >> print(hi_translator.translate(76.05))
    ६७.०५

    >> # Try the Oriya Translator
    >> or_translator = Translator(lang="or")
    >> print(or_translator.translate(123))
    ୧୨୩
    >> print(or_translator.translate("456"))
    ୪୫୬
    >> print(or_translator.translate("There are 456 ducks in the zoo!"))
    There are ୪୫୬ ducks in the zoo!

### Contributing

PRs welcome !