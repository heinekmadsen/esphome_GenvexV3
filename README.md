# esphome_GenvexV3

This repository packages the **GenvexV2** custom component from [`heinekmadsen/esphome_components`](https://github.com/heinekmadsen/esphome_components) so it can be consumed as a standalone ESPHome external component.

> **Important:** The upstream project does not advertise an explicit license at the time of writing. Before distributing or modifying the upstream sources, make sure you have permission from the original author.

## Structure

```
components/           # Local copy of upstream components (populated via scripts)
vendor/esphome_components/  # Git submodule pinned to the upstream repo (latest main)
scripts/              # Sync helpers
esphome/              # Example ESPHome configuration(s)
```

The repository keeps upstream code out of the primary history. Instead, a git submodule (`vendor/esphome_components`) tracks the latest commit on the upstream `main` branch, and the helper script can vendor just the `components/genvexv2` subtree when you want those files under `components/`.

Current submodule pointer (as of this commit): `717f90ae4f27886f1e426e5f9e661edbeb9152f9`.

## Getting started

1. Install the project dependencies:
   - PowerShell 7+
   - `git` (required for the sync helper)
2. Make sure the submodule is checked out (first-time clone only):

   ```powershell
   git submodule update --init --recursive
   ```

3. Pull the latest GenvexV2 component sources into `components/genvexv2`:

   ```powershell
   pwsh scripts/sync_genvexv2.ps1
   ```

4. Point ESPHome at the local checkout when compiling firmware:

   ```yaml
   external_components:
     - source:
         type: local
         path: ./components
       components:
         - genvexv2
   ```

5. Flash the generated firmware to your device.

### Updating to newer upstream commits

Re-run the sync script whenever you want to pull new changes. The helper transparently fetches the latest commit from the `main` branch and replaces the local copy.

## Example ESPHome configuration

See [`esphome/example.yaml`](esphome/example.yaml) for a minimal configuration using the component. Adjust the UART pins and Modbus parameters to match your hardware.

## Roadmap

- ✅ Automate intake of upstream sources via script
- ☐ Add integration tests (requires ESPHome build container)
- ☐ Automate GitHub releases
