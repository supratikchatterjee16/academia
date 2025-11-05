# deployment recipe: perform push to remote for child, followed by pulling parent into ".parent" directory,
# updating submodules, and pushing the changes to remote
PARENT_REPO = https://github.com/supratikchatterjee16/academia-frontend.git

commit:
	git status
	@echo "\n\n\033[1mEnter a commit message for changes(description of changes done):\033[0m"; \
	read msg; \
	git add .; \
	git commit -m "$$msg"; \
	git push origin master

deploy: commit
	@if [ -d .parent/.git ]; then \
		echo "Updating parent..."; \
		git -C .parent pull; \
	else \
		echo "Cloning parent..."; \
		git clone $(PARENT_REPO) .parent; \
		cd .parent; \
		git submodule update --init --recursive; \
	fi
	cd .parent; \
	git submodule update --recursive --remote; \
	git commit -am "Submodule update"; \
	git push origin master
