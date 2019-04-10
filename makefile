run: main.py display.py draw.py matrix.py parse.py transform.py
	python main.py

rungood: maingood.py display.py draw.py matrix.py parse.py transform.py
	python maingood.py

clean:
	rm *.pyc
	rm *~
