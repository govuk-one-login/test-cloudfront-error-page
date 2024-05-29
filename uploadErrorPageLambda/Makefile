build-StaticSiteUploadLayer:
	mkdir -p $(ARTIFACTS_DIR)/static-error-pages
	cp index.html "$(ARTIFACTS_DIR)/static-error-pages"
	mkdir -p "$(ARTIFACTS_DIR)/python"
	cp *.py "$(ARTIFACTS_DIR)/python"
	python -m pip install -r requirements.txt --platform manylinux2014_x86_64 --target "$(ARTIFACTS_DIR)/python" --python-version 3.12