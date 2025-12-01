#pragma once

#include "esphome/core/component.h"
#include "esphome/components/climate/climate.h"
#include "esphome/components/sensor/sensor.h"
#include "esphome/components/number/number.h"

namespace esphome {
namespace genvex {
class GenvexClimate : public climate::Climate, public Component {
public:
  GenvexClimate() {}

  void setup() override;
  void dump_config() override;

  void set_current_temp_sensor(sensor::Sensor *sensor) { this->current_temp_sensor_ = sensor; }
  void set_temp_setpoint_number(number::Number *number) { this->temp_setpoint_number_ = number; }

protected:
  void control(const climate::ClimateCall& call) override;
  climate::ClimateTraits traits() override;

  sensor::Sensor *current_temp_sensor_{ nullptr };
  number::Number *temp_setpoint_number_{ nullptr };
};
}  // namespace genvex
}  // namespace esphome
