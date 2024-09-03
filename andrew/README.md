This directory contains the files necessary for executing a comparison between the keyboarded Sāraḷā Mahābhārata files and the OCR text of the same.

Each volume of Arttaballabha Mohanty's is represented by a single folder, which contains two sets of files:
- mbho01-keyboarded-01.txt
- mbho02-ocr-01.txt
i.e., the keyboarded and OCR text, respectively, of the first page of the first volume. 

The files in those folders are generated from the FULL_TEXT response of a Google Cloud Vision call on each page in the case of the OCR text, and a simple Python script to separate the XML files into pages, with some light postprocessing on each.