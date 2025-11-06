import json
import sys


def load_config(config_path):
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: Конфигурационный файл {config_path} не найден")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле {config_path}")
        sys.exit(1)


def validate_config(config):
    required_params = [
        "package_name",
        "repository_url",
        "test_mode",
        "version"
    ]

    for param in required_params:
        if param not in config:
            print(f"Ошибка: Отсутствует обязательный параметр {param}")
            sys.exit(1)

        if not config[param]:
            print(f"Ошибка: Параметр {param} не может быть пустым")
            sys.exit(1)


def main():
    config = load_config("config.json")
    validate_config(config)

    print("Настраиваемые параметры:")
    for key, value in config.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()