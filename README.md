# dotfiles

dotfiles for macOS, Ubuntu, and Windows

## Installing Tools

### mise

First, install mise from the official web page.\
Then, review, and apply the managed dotfiles from the repository root.

```shell
mise bootstrap dotfiles apply --dry-run
mise bootstrap dotfiles apply
```

### Homebrew

First, install Homebrew from the official web page.\
Then, run the command below.

```shell
brew bundle install --file=tools/Brewfile
```
