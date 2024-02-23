pip install sphinx
pip install -e
sphinx -f --no-toc -d 1 --separate --module-first --output-dir docs/api src/main
sphinx-build -M html . build/
sphinx-build -M latexpdf . build/