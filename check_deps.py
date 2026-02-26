"""Скрипт для проверки установленных зависимостей."""

import sys
import importlib.metadata


def check_package_installed(package_name: str) -> bool:
    """Проверяет, установлен ли пакет."""
    try:
        importlib.metadata.distribution(package_name)
        return True
    except importlib.metadata.PackageNotFoundError:
        return False


def get_package_version(package_name: str) -> str | None:
    """Возвращает версию установленного пакета."""
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return None


def check_dependencies() -> None:
    """Проверяет наличие требуемых зависимостей."""
    # Проверяем виртуальное окружение
    if ".venv" in sys.executable:
        print("Виртуальное окружение АКТИВНО")
    else:
        print("Виртуальное окружение НЕ активно")
    print()

    # Список пакетов для проверки
    required_packages = ["requests", "click", "pydantic"]
    all_installed = True
    for package in required_packages:
        installed = check_package_installed(package)
        version = get_package_version(package)

        if installed:
            print(f"{package:10} установлен: версия {version}")
        else:
            print(f"{package:10} НЕ УСТАНОВЛЕН")
            all_installed = False

    installed_packages = []
    for dist in importlib.metadata.distributions():
        name = dist.metadata.get("Name", "unknown")
        if name and not name.startswith("_"):
            installed_packages.append((name, dist.version))

    for name, ver in sorted(installed_packages):
        print(f"{name:25} {ver}")

    print(f"\nВсего пакетов: {len(installed_packages)}")

def main() -> None:
    check_dependencies()

if __name__ == "__main__":
    main()