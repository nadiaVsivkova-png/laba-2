"""Скрипт проверки версий установленных библиотек."""

import requests
import pydantic

def check_dependencies() -> None:
    """Проверяет версии установленных библиотек.

    Печатает версии библиотек requests и pydantic.
    """
    # Получаем версию requests
    requests_version = requests.__version__
    print(f"requests: {requests_version}")

    # Получаем версию pydantic
    pydantic_version = pydantic.__version__
    print(f"pydantic: {pydantic_version}")

def main() -> None:
    check_dependencies()

if __name__ == "__main__":
    main()