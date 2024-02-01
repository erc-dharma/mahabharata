# ସାରଳା ମହାଭାରତ: Sāraḷā Dāsa's Mahābhārata

The `iast` directory contains the "work" version viz. the one that should be
amended if need be.

The `ori` directory contains an automatic conversion in the Oriya script of the
contents of the `iast` directory. The conversion is done with `translit.py`. To
update the `ori` directory, run:

	make

The file `missing_alpha.txt` contains a frequency table of alphabetic characters
in `iast` that are not converted to the Oriya script. These are characters we do
not know how to transliterate.

The `orig` directory contains Arlo's original data (which dates from august
2009). Within this dir, `Text_Files_(UR)` (in IAST) is generated from
`Text_Files_(Malten)` (in SLP1 or sth) and is newer by a week. The date of
`Text_files_problems` is unknown. We assume the IAST data is up-to-date and
ignore the original data. We don't have access to the original converter.
Apparently, there are transliteration problems between the original (Malten) and
the generated (UR).
