# The relevant Unicode chart is at https://www.unicode.org/charts/PDF/U0B00.pdf

import sys, os, unicodedata

L = lambda s: unicodedata.lookup("oriya letter %s" % s)
D = lambda s: unicodedata.lookup("oriya digit %s" % s)
S = lambda s: unicodedata.lookup("oriya vowel sign %s" % s)

initial_vowels = {
	"a": L("a"),
	"ā": L("aa"),
	"i": L("i"),
	"ī": L("ii"),
	"u": L("u"),
	"ū": L("uu"),
	"r\N{combining ring below}": L("vocalic r"),
	"r\N{combining ring below}\N{combining macron}": L("vocalic rr"),
	"l\N{combining ring below}": L("vocalic l"),
	"l\N{combining ring below}\N{combining macron}": L("vocalic ll"),
	"e": L("e"),
	"ai": L("ai"),
	"o": L("o"),
	"au": L("au"),
}

intra_vowels = {
	"ā": S("aa"),
	"i": S("i"),
	"ī": S("ii"),
	"u": S("u"),
	"ū": S("uu"),
	"r\N{combining ring below}": S("vocalic r"),
	"r\N{combining ring below}\N{combining macron}": S("vocalic rr"),
	"l\N{combining ring below}": S("vocalic l"),
	"l\N{combining ring below}\N{combining macron}": S("vocalic ll"),
	"e": S("e"),
	"ai": S("ai"),
	"o": S("o"),
	"au": S("au"),
}

consonants = {
	"k": L("ka"),
	"kh": L("kha"),
	"g": L("ga"),
	"gh": L("gha"),
	"ṅ": L("nga"),

	"c": L("ca"),
	"ch": L("cha"),
	"j": L("ja"),
	"jh": L("jha"),
	"ñ": L("nya"),

	"ṭ": L("tta"),
	"ṭh": L("ttha"),
	"ḍ": L("dda"),
	"ḍh": L("ddha"),
	"ṇ": L("nna"),

	"t": L("ta"),
	"th": L("tha"),
	"d": L("da"),
	"dh": L("dha"),
	"n": L("na"),

	"p": L("pa"),
	"ph": L("pha"),
	"b": L("ba"),
	"bh": L("bha"),
	"m": L("ma"),

	"y": L("ya"),
	"r": L("ra"),
	"l": L("la"),
	"v": L("va"),

	"ś": L("sha"),
	"ṣ": L("ssa"),
	"s": L("sa"),
	"h": L("ha"),

	"ḷ": L("lla"),
	"ẏ": L("yya"),
}

other = {
	"0": D("zero"),
	"1": D("one"),
	"2": D("two"),
	"3": D("three"),
	"4": D("four"),
	"5": D("five"),
	"6": D("six"),
	"7": D("seven"),
	"8": D("eight"),
	"9": D("nine"),
	"|": "\N{devanagari danda}",
	"||": "\N{devanagari double danda}",
	"'": "\N{oriya sign avagraha}",
	"ḥ": "\N{oriya sign visarga}",
	"ṃ": "\N{oriya sign anusvara}",
}

charset = sorted(initial_vowels | intra_vowels | consonants | other, key=len, reverse=True)
assert set(initial_vowels).issuperset(intra_vowels)

def next_char(s):
	assert s
	for c in charset:
		if s.startswith(c):
			return c, s[len(c):]
	# Unknown
	print(s[0], file=sys.stderr)
	return s[0], s[1:]

virama = "\N{oriya sign virama}"

def translit(s):
	buf = []
	prev_c = None
	while s:
		c, s = next_char(s)
		if prev_c in consonants:
			if c == "a":
				pass
			elif c in intra_vowels:
				buf.append(intra_vowels[c])
			else:
				buf.append(virama)
				buf.append(consonants.get(c) or other.get(c, c))
		elif prev_c not in charset or prev_c == "||" or prev_c in "|0123456789":
			if c in initial_vowels:
				buf.append(initial_vowels[c])
			else:
				buf.append(consonants.get(c) or other.get(c, c))
		else:
			buf.append(intra_vowels.get(c) or consonants.get(c) or other.get(c, c))
		prev_c = c
	return "".join(buf)

def translit_file(inp, out):
	for line in inp:
		assert line.endswith("\n")
		line = unicodedata.normalize("NFC", line)
		ret = translit(line)
		out.write(ret)

if __name__ == "__main__":
	translit_file(sys.stdin, sys.stdout)
