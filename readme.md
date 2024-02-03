# ସାରଳା ମହାଭାରତ: Sāraḷā Dāsa's Mahābhārata
# Notes by Arlo Griffiths and Michaël Meyer, February 2024

Scans of Arttaballabha Mohanty's edition are available at
https://archive.org/details/odia-mahabharata.

The edition was scanned in 2008 at Leiden University by Arlo Griffiths with the
help of his assistant Shila Schoots. Based on these scans, the edition was
rekeyed 2009 by typists based in South India whose work was coordinated by
Thomas Malten. The work was done at the time with a low budget furnished by Arlo
Griffiths and left a lot to be desired. It has remained dormant for nearly 15
years and has now (Febr. 2024) started to be gradually cleaned up.

For reasons we cannot reconstruct, vol. 2 is missing from scans but is available
in plain text.

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
in `iso` that are not converted to the Oriya script. These are characters which
may not need transliteration or whose correct transliteration we have not yet
determined at this time.

The `orig` directory contains the original data obtained by Arlo Griffiths from
Thomas Malten. Within this dirrectory, `Text_Files_(UR)` (in IAST) is generated
from `Text_Files_(Malten)` (in some variant of the Harvard-Kyoto scheme) and is
newer by a week. The file `Text_files_problems` was created and last edited on
2009-08-21. We assume that the IAST data is up-to-date and ignore the original
data. We don't have access to the original converter. Apparently, there are
transliteration problems between the original files (received from Malten) and
the files (UR) generated from them.

To help identify problems, Michaël Meyer has created three additional files:
`malten_full.txt`, `iso_full.txt` and `ori_full.txt`. They hold the full text of
the respective versions, concatenated into a single file, and without markers.

There are about 40 less lines in malten_full than in iso_full and ori_full,
probably because some markers from malten_full where incorrectly transliterated.
