env: 
	python3 -m venv env
	env/bin/pip install -U setuptools
	env/bin/pip install -U pip
	env/bin/pip install -r offv_api/requirements.pip
	env/bin/pip install -e offv_api


test-env: env
	env/bin/pip install -r offv_api/test-requirements.pip

test: test-env
	env/bin/pytest


init: env
	env/bin/flask db upgrade

db_migrate: env
	env/bin/flask db migrate


build: env
	cd frontend; npm run build

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

dist-clean: clean
	bin/db_clean
