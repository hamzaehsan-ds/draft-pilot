# Draft Pilot API prototype

This folder contains the Python command-line email-drafting prototype. It uses
LangChain with the `gemma4:31b-cloud` model through Ollama. It is not an HTTP
server at this stage.

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)
- [Ollama](https://ollama.com/) configured to use `gemma4:31b-cloud`

## Setup and run

From this folder:

```bash
uv sync
uv run python -m app.main
```

Enter an email idea at the prompt. The agent prints a drafted email with a
subject, greeting, body, and sign-off.

See the [project README](../README.md) for instructions for the web starter.
