all: clean update-readme

update-readme:
	cp assets/base_README.md assets/README.md
	echo "<pre>" >> assets/README.md
	tree . >> assets/README.md
	echo "</pre>" >> assets/README.md
	mv assets/README.md .
	rm -rf assets/README.md

clean:
	rm -rf src/*.out src/*.class

