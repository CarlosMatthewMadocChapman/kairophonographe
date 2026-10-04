.PHONY: validate test api example

validate:
	python scripts/validate_repo.py

test:
	pytest -q

api:
	uvicorn api.app:app --reload

example:
	python scripts/render_example.py examples/new-terrain/session.json
