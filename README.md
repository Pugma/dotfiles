# dotfiles

dotfiles for macOS, Ubuntu, and Windows

## Installing Tools

### Native installation

Install these tools with their native installers.

- Codex CLI
- uv
- rustup

### mise

Install mise from the official website.\
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
