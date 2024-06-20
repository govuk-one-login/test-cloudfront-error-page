build-StaticSiteUploadFunction:
	mkdir -p $(ARTIFACTS_DIR)/static-error-pages
	cp index.html "$(ARTIFACTS_DIR)/static-error-pages"

	cp requirements.txt "$(ARTIFACTS_DIR)"
	cp *.py "$(ARTIFACTS_DIR)"
	python -m pip install -r requirements.txt --platform manylinux2014_x86_64 --target "$(ARTIFACTS_DIR)" --python-version 3.12
	rm -rf $(ARTIFACTS_DIR)/bin
