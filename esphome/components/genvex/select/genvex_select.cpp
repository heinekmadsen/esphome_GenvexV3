#include "genvex_select.h"
#include "esphome/core/log.h"

namespace esphome {
namespace genvex {
static const char *TAG = "genvex.select";

void GenvexSpeedSelect::dump_config() {
  LOG_SELECT("", "Genvex Select", this);
}

void GenvexSpeedSelect::control(const std::string &value) {
  if (this->traits.get_options().empty()) {
    ESP_LOGW(TAG, "No options configured");
    return;
  }
  auto *target_number = this->speed_number_ != nullptr ? this->speed_number_ : this->timer_number_;
  if (target_number == nullptr) {
    ESP_LOGW(TAG, "No bound number configured (speed/timer)");
    return;
  }
  const auto &options = this->traits.get_options();
  for (size_t i = 0; i < options.size(); ++i) {
    if (options[i] == value) {
      ESP_LOGD(TAG, "Setting index: %d", (int)i);
      target_number->make_call().set_value(static_cast<float>(i)).perform();
      this->publish_state(value);
      return;
    }
  }
  ESP_LOGW(TAG, "Unknown select option: %s", value.c_str());
}

}  // namespace genvex
}  // namespace esphome
