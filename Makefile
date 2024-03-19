setup: environment.yml
	@echo Installing Conda environment
	conda env update --prune --file $^
	# @$(TOUCH) $@
