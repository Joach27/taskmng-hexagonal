# taskmng-hexagonal

Minimal task management example using hexagonal architecture.

## Structure

- `taskmng/domain`: core domain models.
- `taskmng/application`: use cases and ports.
- `taskmng/adapters`: concrete implementations of ports.
- `tests`: focused unit tests.

## Run tests

```bash
python -m unittest discover -v
```
