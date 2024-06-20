build-StaticSiteUploadFunction:
	mkdir -p $(ARTIFACTS_DIR)/static-error-pages
	cp index.html "$(ARTIFACTS_DIR)/static-error-pages"

	cp requirements.txt "$(ARTIFACTS_DIR)"
	cp *.py "$(ARTIFACTS_DIR)"
	python -m pip install -r requirements.txt --target "$(ARTIFACTS_DIR)"
	rm -rf $(ARTIFACTS_DIR)/bin
