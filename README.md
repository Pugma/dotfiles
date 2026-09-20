# dotfiles

dotfiles for macOS, Ubuntu, and Windows

## Installing Tools

### Native installation

Install these tools with their native installers.

- Codex CLI
- uv
- rustup

### mise

Install mise 2026.7.4 or later from the official website.\
From the repository root, copy the local Git config template, review it, then apply the managed dotfiles.

```shell
cp git/config.local.example git/config.local
mise bootstrap dotfiles apply --dry-run
mise bootstrap dotfiles apply
```

### Homebrew

Install Homebrew from the official website.\
Then install the packages in the Brewfile.

```shell
brew bundle install --file=tools/Brewfile
```

### Windows

Use PowerShell & winget to install Git & mise.

```powershell
winget install --id Git.Git -e --source winget
winget install --id jdx.mise -e
```

refs:\
https://git-scm.com/install/windows\
https://mise.jdx.dev/installing-mise.html

Restart PowerShell after installation.\
Update tools installed this way with winget; do not use `mise self-update` for a winget-managed mise installation.

```powershell
winget upgrade --id Git.Git -e
winget upgrade --id jdx.mise -e
```
