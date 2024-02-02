# ସାରଳା ମହାଭାରତ: Sāraḷā Dāsa's Mahābhārata

Scans are available at https://archive.org/details/odia-mahabharata. Vol. 2 is missing from scans but is available in plain text.

Portions of the text are missing in the plain text version:

* vol. 1 part 2 pp. 1058-9 (also missing in scans)
* vol. 2 part 1 pp. 60-5, 219-21, 237-9; part 2 pp. 676-7, 1125-40
* vol. 3 part 2 pp. 632, 652
* vol. 5 pp. 164-5 (also missing in scans)
* vol. 6 p. 344
* vol. 10 part 4
* vol. 11 part 3 pp. 214-5 (also missing in scans)

Vol. 7 in particular was not input reliably.

The `iso` directory contains the "work" version viz. the one that should be
amended if need be.

The `ori` directory contains an automatic conversion in the Oriya script of the
contents of the `iso` directory. The conversion is done with `translit.py`. To
update the `ori` directory, run:

	make

The file `missing_alpha.txt` contains a frequency table of alphabetic characters
in `iso` that are not converted to the Oriya script. These are characters we do
not know how to transliterate.

The `orig` directory contains Arlo's original data (which dates from august
2009). Within this dir, `Text_Files_(UR)` (in IAST) is generated from
`Text_Files_(Malten)` (in SLP1 or some such encoding) and is newer by a week. The file
`Text_files_problems` was created and last edited on 2009-08-21. We assume that the IAST data is up-to-date and
ignore the original data. We don't have access to the original converter.
Apparently, there are transliteration problems between the original (Malten) and
the generated (UR).

To help identify problems, I created three additional files: `malten_full.txt`, `iso_full.txt` and `ori_full.txt`. They hold the full text of the respective versions, concatenated into a single file, and without markers.

There are about 40 less lines in malten_full than in iso_full and ori_full, probably because some markers from malten_full where incorrectly transliterated. In malten_full itself, there are quite a few weird character sequences, like "coÔøΩkhaÔøΩ", which are preserved in iso_full but obviously should have been transliterated to something more meaningful.
