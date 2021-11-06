buildall:
	# 1. Build the frontend
	npm run build
	# 2. Move files at the build root inside a root subdirectory
	cp build/static/js/main.*.js ../../rmp/static/js/main.js
	cp build/static/css/main.*.css ../../rmp/static/css/main.css
run:
	npm run start