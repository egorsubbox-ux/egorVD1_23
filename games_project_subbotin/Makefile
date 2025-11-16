# Установка зависимостей
install:
	uv sync

# Запуск игр
VD-games:
	uv run VD-games

VD-even:
	uv run VD-even

VD-calc:
	uv run VD-calc

VD-gcd:
	uv run VD-gcd

VD-progression:
	uv run VD-progression

VD-prime:
	uv run VD-prime

# Сборка пакета
build:
	uv build

# Установка пакета в систему
package-install:
	uv tool install dist/*.whl

# Переустановка пакета
reinstall:
	uv tool install --force dist/*.whl

# Проверка кода линтером
lint:
	uv run ruff check VD_games
