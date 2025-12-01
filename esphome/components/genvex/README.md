# Genvex ESPHome Component (fresh scaffold)

This component provides a minimal integration for Genvex devices over Modbus via ESPHome.

## Features
- Climate (`genvex.climate`): single target temperature, current temperature, optional fan speed mapping.
- Selects (`genvex.select`):
  - Speed (Off/1–4) bound to a Modbus `number`.
  - Timer (Off/1–9) bound to a Modbus `number`.

## YAML Wiring (example)
See `esphome/example_genvex.yaml` for a complete example including Modbus numbers/sensors and component usage.

Key bindings:
- `genvex_id`: root component instance.
- `current_temp_sensor_id`: Modbus sensor (e.g., address 6).
- `target_temp_number_id`: Modbus number (e.g., address 0) with `write_lambda` for °C conversion.
- `fan_speed_number_id`: Modbus number (e.g., address 100) mapping 0..4.
- Speed Select: `speed_number_id` to the same number as `fan_speed_number_id`.
- Timer Select: `timer_number_id` (e.g., address 106).

## Notes
- Climate fan state mirrors speed number: OFF↔0, custom modes "1".."4" ↔ 1..4.
- Selects write indices to their bound `number` and publish the chosen option.
- Adjust Modbus addresses and conversions according to your device documentation.
