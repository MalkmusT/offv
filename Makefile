build:
	python3 -m venv env
	env/bin/pip install -r api/requirements.pip
	npm run build


clean:
	rm -f release.tar.gz
	rm -rf api/env
	rm -rf build/

package:
	tar cf release.tar.gz build/ 
	tar cf release.tar.gz api/
	
