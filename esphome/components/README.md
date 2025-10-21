# components/

This directory holds the ESPHome external components that ship with `esphome_GenvexV3`.

Run `pwsh scripts/sync_genvexv2.ps1` to populate the `genvexv2` component from the upstream repository. The script consults the vendored git submodule (`vendor/esphome_components`) when available and otherwise falls back to a shallow clone of the upstream `main` branch.
