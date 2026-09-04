# AGENTS.md

## Scope

- Personal dotfiles for macOS and Ubuntu.
- Support WSL; support native Windows only as needed for Git-based Unity work.
- Prioritize a simple, maintainable, and portable bootstrap over full environment reproducibility.
- Use each tool's native update mechanism.

## Ownership

Do not manage the same tool or configuration in multiple places.

- `mise`
  - user dotfiles managed with `mise bootstrap dotfiles`
  - runtimes except for Python & Rust
  - development CLI tools
- `uv`
  - Python versions
  - Python packages
  - Python scripts
- `rustup`
  - Rust toolchains
- Homebrew
  - macOS CLI tools
  - non-GUI casks
  - GUI application casks are currently out of scope
- `apt`
  - Ubuntu/WSL system packages
- Native installers
  - tools not assigned above, using their normal update flow

## mise bootstrap dotfiles

- Inspect existing target files before adding or applying them.
- Add or update managed sources explicitly with `mise bootstrap dotfiles add`.
- During migration, the current machine is the source of truth; preserve existing settings and shell behavior.

## Workflow

- When dotfile mappings change, review `mise bootstrap dotfiles apply --dry-run`.
- Before committing, run `mise run fmt:toml` and then `mise run check`.
- Review the resulting `git diff` and run `git diff --check`.
- Never commit credentials, tokens, private keys, or login state.
- Preserve unrelated working-tree changes and explain destructive or external changes before executing them.
- Commit small, scoped changes with concise English Conventional Commit messages; never push without an explicit request.
