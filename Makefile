env: 
	python3 -m venv env
	env/bin/pip install -r api/requirements.pip


build: env
	npm run build


package: build
	tar cf release.tar.gz build/ 
	tar rf release.tar.gz api/


deploy: package
	scp release.tar.gz offv@verena-tobias.de:~/
	ssh offv@verena-tobias.de ./bin/restart

clean:
	rm -f release.tar.gz
	rm -rf env/
	rm -rf api/__pycache__
	rm -rf build/

