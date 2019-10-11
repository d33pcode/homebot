install:
	@( \
		echo "adjusting configuration..."; \
		mkdir -p log; \
		[ -e "config.yaml" ] || cp config.yaml.example config.yaml; \
		echo "checking virtual environment..."; \
		test -d venv || python3 -m venv venv; \
		source venv/bin/activate; \
		echo "installing dependencies..."; \
		pip install -r requirements.txt; \
	);

clean:
	@( \
		echo "deactivating environment..."; \
		command -v deactivate && deactivate; \
		echo "cleaning up folders..."; \
		rm -rf log venv __pycache__; \
	);
