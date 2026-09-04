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

### Editor settings

Editor settings are applied according to the OS where `mise` is run.

| OS | VS Code | Zed |
| --- | --- | --- |
| macOS | `~/Library/Application Support/Code/User/settings.json` | `~/.config/zed/settings.json` |
| Linux | — | `~/.config/zed/settings.json` |
| Windows | `~/AppData/Roaming/Code/User/settings.json` | `~/AppData/Roaming/Zed/settings.json` |

The Linux mapping assumes Zed's default configuration root, `~/.config`.
Custom `XDG_CONFIG_HOME` locations are not supported by this mapping.

The Windows mappings assume the default profile layout, where
`~/AppData/Roaming` corresponds to `%APPDATA%`. Redirected `%APPDATA%`
locations are not supported by these mappings.

To configure Windows-native VS Code or Zed from WSL, install mise for Windows,
clone this repository to `%USERPROFILE%\develop\dotfiles` on the Windows
filesystem, and run the following from the Windows checkout in PowerShell.
`git/config.local` is intentionally untracked, so it must be initialized and
reviewed separately in this checkout before applying all dotfiles.

```powershell
if (-not (Test-Path -LiteralPath git/config.local)) {
  Copy-Item -LiteralPath git/config.local.example -Destination git/config.local
}
notepad.exe git/config.local
mise bootstrap dotfiles apply --dry-run
mise bootstrap dotfiles apply
```

Running mise inside WSL only configures Linux applications and cannot configure
the Windows-native editors.

#### Migrating existing editor links

Older revisions applied both editor mappings on every OS. After updating an
existing checkout, remove the following legacy paths only when they are symbolic
links to the listed source in the checkout that created them. Preserve regular
files, copied files, and links to any other source.

| OS | Legacy path | Expected source |
| --- | --- | --- |
| Linux / WSL | `~/Library/Application Support/Code/User/settings.json` | `<checkout>/editors/vscode-settings.jsonc` |
| Windows | `~/.config/zed/settings.json` | `<checkout>/editors/zed-settings.jsonc` |
| Windows | `~/Library/Application Support/Code/User/settings.json` | `<checkout>/editors/vscode-settings.jsonc` |

No cleanup is needed on macOS because both legacy targets remain managed.

### Homebrew

Install Homebrew from the official website.\
Then install the packages in the Brewfile.

```shell
brew bundle install --file=tools/Brewfile
```
