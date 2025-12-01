#include "genvex_climate.h"
#include "esphome/core/log.h"

namespace esphome {
namespace genvex {
static const char *TAG = "genvex.climate";

void GenvexClimate::setup() {
  if (current_temp_sensor_ != nullptr) {
    current_temp_sensor_->add_on_state_callback([this](float state) {
      this->current_temperature = state;
      this->publish_state();
    });
    this->current_temperature = current_temp_sensor_->state;
  }
  if (temp_setpoint_number_ != nullptr) {
    temp_setpoint_number_->add_on_state_callback([this](float state) {
      this->target_temperature = state;
      this->publish_state();
    });
    this->target_temperature = temp_setpoint_number_->state;
  }
  this->publish_state();
}

void GenvexClimate::control(const climate::ClimateCall& call) {
  if (call.get_target_temperature().has_value() && temp_setpoint_number_ != nullptr) {
    float target = *call.get_target_temperature();
    ESP_LOGD(TAG, "Setting target temperature: %f", target);
    temp_setpoint_number_->make_call().set_value(target).perform();
    this->target_temperature = target;
  }
  if (call.get_mode().has_value()) {
    this->mode = *call.get_mode();
  }
  this->publish_state();
}

climate::ClimateTraits GenvexClimate::traits() {
  auto traits = climate::ClimateTraits();
  traits.set_supported_modes({
    climate::ClimateMode::CLIMATE_MODE_OFF,
    climate::ClimateMode::CLIMATE_MODE_HEAT,
  });
  traits.set_visual_temperature_step(0.1f);
  traits.set_visual_min_temperature(5.0f);
  traits.set_visual_max_temperature(30.0f);
  traits.set_supports_current_temperature(true);
  traits.set_supports_two_point_target_temperature(false);
  traits.set_supports_action(true);
  return traits;
}

void GenvexClimate::dump_config() {
  LOG_CLIMATE("", "Genvex Climate", this);
}

}  // namespace genvex
}  // namespace esphome
