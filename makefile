input := $(wildcard iso/*.txt)
output := $(addprefix ori/,$(notdir $(input)))

all: $(output)

debug:
	cat iso/* | python3 ~/dharma/cleanup.py | sed -e 's,<[^>]*>,,g ; /MBO/d' > iso_full.txt
	python3 translit.py < iso_full.txt 1> ori_full.txt 2> missing_alpha.txt
	grep -Ev '[[:cntrl:]]|[[:space:]]|[[:punct:]]' missing_alpha.txt | grep . | freq > tmp && mv tmp missing_alpha.txt

.PHONY: all debug

ori/%.txt: iso/%.txt translit.py
	mkdir -p ori
	python3 translit.py < "$<" > "$@"
