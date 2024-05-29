build-StaticSiteUploadLayer:
	mkdir -p $(ARTIFACTS_DIR)/static-error-pages
	cp index.html "$(ARTIFACTS_DIR)/static-error-pages"
	mkdir -p "$(ARTIFACTS_DIR)/python"
	cp *.py "$(ARTIFACTS_DIR)/python"
	python -m pip install -r requirements.txt -t "$(ARTIFACTS_DIR)/python"
