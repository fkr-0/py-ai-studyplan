.PHONY: slides serve test check site

slides:
	python3 scripts/build_slides.py

site: slides
	python3 scripts/stage_pages.py

serve: check
	python3 -m http.server 8765 --bind 127.0.0.1 --directory _site

test:
	python3 -m unittest discover -s tests -v
	python3 -m unittest discover -s examples/tests -v

check: slides test
	python3 scripts/check_project.py
	python3 scripts/validate_course.py
	python3 -m compileall -q examples tests scripts
	python3 scripts/stage_pages.py
	python3 scripts/check_site.py
