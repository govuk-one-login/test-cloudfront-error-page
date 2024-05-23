build-StaticSiteUploadLayer:

	# Copy in to the layer the single index.html containing all needed assets inlined in the file:

	mkdir -p $(ARTIFACTS_DIR)/static-error-pages
	cp ../../index.html "$(ARTIFACTS_DIR)/static-error-pages"

	# Copy in to the layer an assets directory containing the assets:
	# 
	# for file in $(find assets -type f);
	# do
	#   mkdir -p $(ARTIFACTS_DIR)/static-error-pages/$(dirname $file)
	#   cp $file $(ARTIFACTS_DIR)/static-error-pages/$(dirname $file)
	# done
