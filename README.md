# my-package

A Python template project using [uv](https://docs.astral.sh/uv/) for dependency management and [Task](https://taskfile.dev/) for task running.

## Features

- **uv** - Fast Python package manager and project tool
- **Task** - Simple, powerful task runner via `Taskfile.yml`
- **Ruff** - Extremely fast Python linter and formatter
- **mypy** - Static type checking
- **pytest** - Testing with coverage reporting
- **pre-commit** - Git hooks for code quality
- **GitHub Actions** - CI/CD pipeline for multi-platform, multi-Python testing

## Requirements

- [uv](https://docs.astral.sh/uv/getting-started/installation/) - `curl -LsSf https://astral.sh/uv/install.sh | sh`
- [Task](https://taskfile.dev/installation/) - `sh -c "$(curl --location https://taskfile.dev/install.sh)" -- -d -b /usr/local/bin`

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/my-package.git
cd my-package

# Set up development environment
task dev

# Run checks
task check
```

## Available Tasks

Run `task` or `task --list` to see all available tasks.

| Task | Description |
|------|-------------|
| `task install` | Install all dependencies (including dev) |
| `task install-prod` | Install production dependencies only |
| `task update` | Update all dependencies |
| `task format` | Format code with ruff |
| `task format-check` | Check formatting without changes |
| `task lint` | Lint code with ruff |
| `task lint-fix` | Lint and auto-fix with ruff |
| `task typecheck` | Type check with mypy |
| `task test` | Run tests with coverage |
| `task test-fast` | Run tests without coverage |
| `task check` | Run all checks |
| `task pre-commit-install` | Install pre-commit hooks |
| `task pre-commit-run` | Run pre-commit on all files |
| `task clean` | Clean build artifacts |
| `task build` | Build the package |
| `task dev` | Full dev setup (install + pre-commit) |

## Project Structure

```
my-package/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI
├── src/
│   └── my_package/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .pre-commit-config.yaml
├── .python-version
├── pyproject.toml          # Project config (uv, ruff, mypy, pytest)
├── Taskfile.yml            # Task definitions
└── README.md
```

## Development Workflow

```bash
# Install dependencies
task install

# Format code
task format

# Run linter
task lint

# Type check
task typecheck

# Run tests
task test

# Run everything
task check
```

## Customization

1. Replace `my-package` / `my_package` with your actual package name
2. Update author info in `pyproject.toml`
3. Update repository URLs in `pyproject.toml`
4. Add your dependencies to `[project] dependencies` in `pyproject.toml`
5. Add dev dependencies to `[dependency-groups] dev` in `pyproject.toml`

## License

MIT
