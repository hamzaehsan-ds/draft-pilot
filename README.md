# Draft Pilot

Draft Pilot is an early-stage email drafting project. The API folder currently
contains a command-line prototype that uses LangChain and an Ollama-hosted
Gemma model to draft emails. The web folder is a Next.js starter and is not
connected to the prototype yet.

## Project structure

```text
draft-pilot/
├── api/   Python email-drafting CLI
└── web/   Next.js web starter
```

## Requirements

- Python 3.13 or newer
- [uv](https://docs.astral.sh/uv/)
- Node.js and npm
- [Ollama](https://ollama.com/) configured to use `gemma4:31b-cloud`

## Run the email-drafting CLI

```bash
cd api
uv sync
uv run python -m app.main
```

When prompted, enter an idea for an email. The prototype asks the configured
model to return a complete email with a subject, greeting, body, and sign-off.

## Run the web starter

```bash
cd web
npm ci
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) to view the Next.js
development server. The current page is the default starter page; it does not
yet call the email-drafting CLI.

## Development commands

From `web/`:

```bash
npm run lint
npm run build
```

From `api/`:

```bash
uv sync
uv run python -m app.main
```

## Current limitations

- The API is currently an interactive command-line script, not an HTTP API.
- The web app is not integrated with the email-drafting prototype.
- The model identifier is configured in `api/app/main.py`; Ollama access to
  that model must be configured in your environment.
