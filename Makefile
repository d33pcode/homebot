install:
	@( \
		echo "installing dependencies..."; \
		mkdir -p log; \
		if [ ! -e "config.yaml"]; then cp config.yaml.example config.yaml; fi; \
		test -d venv || python3 -m venv venv; \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)

clean:
	@( \
		command -v deactivate && deactivate; \
		rm -rf log venv __pycache__; \
	)
