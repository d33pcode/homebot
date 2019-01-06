install:
	@( \
		mkdir -p log; \
		test -d venv || python3 -m venv venv; \
		source venv/bin/activate; \
		pip install -r requirements.txt; \
	)

clean:
	@( \
		command -v deactivate && deactivate; \
		rm -rf log venv __pycache__; \
	)
