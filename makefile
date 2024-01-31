input := $(wildcard iast/*.txt)
output := $(addprefix ori/,$(notdir $(input)))

all: $(output)

.PHONY: all

ori/%.txt: iast/%.txt translit.py
	mkdir -p ori
	python3 translit.py < "$<" > "$@"
