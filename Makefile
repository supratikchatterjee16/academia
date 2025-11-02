# deployment recipe: perform push to remote for child, followed by pulling parent into ".parent" directory,
# updating submodules, and pushing the changes to remote
PARENT_REPO = https://github.com/supratikchatterjee16/academia-frontend.git

commit:
	@echo "Enter a commit message: "; \
	read msg; \
	git add .; \
	git commit -m "$$msg"; \
	git push origin master; \
	-mkdir .parent; \
	cd .parent; \

deploy: commit
	@if [ -d .parent/.git ]; then \
		echo "Updating parent..."; \
		git -C .parent pull; \
	else \
		echo "Cloning parent..."; \
		git clone $(PARENT_REPO) .parent; \
	fi
	cd .parent; \
	git submodule update --remote --merge; \
	git add .; \
	echo "Enter a commit message for parent: "; \
	read pmsg; \
	git commit -m "$$pmsg"; \
	git push origin master;
