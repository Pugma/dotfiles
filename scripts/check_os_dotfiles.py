#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///

"""Validate the OS-specific editor mappings composed by mise."""

from __future__ import annotations

import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
from typing import Any


ROOT = Path(__file__).resolve().parents[1]

EDITOR_TARGETS = {
    "~/.config/zed/settings.json",
    "~/Library/Application Support/Code/User/settings.json",
    "~/AppData/Roaming/Code/User/settings.json",
    "~/AppData/Roaming/Zed/settings.json",
}

PROFILES = {
    "linux": {
        "environments": ("unix",),
        "mappings": {
            "~/.config/zed/settings.json": "editors/zed-settings.jsonc",
        },
    },
    "macos": {
        "environments": ("unix", "macos"),
        "mappings": {
            "~/.config/zed/settings.json": "editors/zed-settings.jsonc",
            "~/Library/Application Support/Code/User/settings.json": (
                "editors/vscode-settings.jsonc"
            ),
        },
    },
    "windows": {
        "environments": ("windows",),
        "mappings": {
            "~/AppData/Roaming/Code/User/settings.json": (
                "editors/vscode-settings.jsonc"
            ),
            "~/AppData/Roaming/Zed/settings.json": "editors/zed-settings.jsonc",
        },
    },
}


def current_profile() -> str:
    if sys.platform == "darwin":
        return "macos"
    if sys.platform == "win32":
        return "windows"
    if sys.platform.startswith("linux"):
        return "linux"
    raise RuntimeError(f"unsupported test platform: {sys.platform}")


def load_status(
    temporary_root: Path, environments: tuple[str, ...] | None
) -> dict[str, Any]:
    env = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(("MISE_", "RTX_"))
    }
    env.update(
        {
            "MISE_CACHE_DIR": str(temporary_root / "cache"),
            "MISE_CEILING_PATHS": str(ROOT.parent),
            "MISE_CONFIG_DIR": str(temporary_root / "config"),
            "MISE_DATA_DIR": str(temporary_root / "data"),
            "MISE_GLOBAL_CONFIG_FILE": str(temporary_root / "global.toml"),
            "MISE_NO_UPDATE_NOTIFIER": "1",
            "MISE_STATE_DIR": str(temporary_root / "state"),
            "MISE_SYSTEM_CONFIG_DIR": str(temporary_root / "system"),
            "MISE_TRUSTED_CONFIG_PATHS": str(ROOT),
            "NO_COLOR": "1",
        }
    )

    command = ["mise"]
    if environments is not None:
        env["MISE_AUTO_ENV"] = "false"
        command.extend(("--env", ",".join(environments)))
    command.extend(("bootstrap", "dotfiles", "status", "--json"))

    result = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"{' '.join(command)} failed with exit code {result.returncode}:\n"
            f"{result.stderr}"
        )
    return json.loads(result.stdout)


def validate_profile(label: str, status: dict[str, Any], profile: str) -> list[str]:
    expected = PROFILES[profile]["mappings"]
    editor_entries = [
        entry for entry in status["files"] if entry["target"] in EDITOR_TARGETS
    ]
    actual_targets = [entry["target"] for entry in editor_entries]
    errors: list[str] = []

    if len(actual_targets) != len(set(actual_targets)):
        errors.append(f"{label}: duplicate editor targets: {actual_targets}")

    if set(actual_targets) != set(expected):
        errors.append(
            f"{label}: expected editor targets {sorted(expected)}, "
            f"got {sorted(actual_targets)}"
        )

    for entry in editor_entries:
        target = entry["target"]
        if target not in expected:
            continue
        expected_source = (ROOT / expected[target]).resolve()
        source_value = entry.get("origin", {}).get("source", entry["source"])
        source = Path(source_value).expanduser().resolve()
        if not expected_source.is_file():
            errors.append(f"{label}: expected source file is missing: {expected_source}")
        if entry.get("state") == "source_missing":
            errors.append(f"{label}: {target} reports a missing source")
        if source != expected_source:
            errors.append(
                f"{label}: {target} source is {source}, "
                f"expected {expected_source}"
            )

    return errors


def main() -> int:
    errors: list[str] = []
    with tempfile.TemporaryDirectory(prefix="mise-os-dotfiles-") as temporary_dir:
        temporary_root = Path(temporary_dir)
        host_profile = current_profile()
        errors.extend(
            validate_profile(
                f"automatic {host_profile}",
                load_status(temporary_root, None),
                host_profile,
            )
        )

        for profile, definition in PROFILES.items():
            errors.extend(
                validate_profile(
                    f"isolated {profile}",
                    load_status(temporary_root, definition["environments"]),
                    profile,
                )
            )

    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1

    print(
        "OS-specific dotfile mappings are correct for the host and all "
        "isolated profiles."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
