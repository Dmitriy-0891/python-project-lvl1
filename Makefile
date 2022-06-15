install:
	poetry install

brain-games:
	poetry run brain-games

brain-calc:
	poetry run brain-calc-game

brain-even:
	poetry run brain-even-game

brain-gcd:
	poetry run brain-gcd-game

brain-prime:
	poetry run brain-prime-game

brain-progression:
	poetry run brain-progression-game

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games
