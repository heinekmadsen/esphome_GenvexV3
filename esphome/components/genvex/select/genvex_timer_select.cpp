#include "genvex_timer_select.h"
#include "esphome/core/log.h"

namespace esphome {
namespace genvex {
static const char *TAG = "genvex.timer_select";

void GenvexTimerSelect::dump_config() {
  LOG_SELECT("", "Genvex Timer Select", this);
}

void GenvexTimerSelect::control(const std::string &value) {
  if (this->traits.get_options().empty() || this->timer_number_ == nullptr) {
    ESP_LOGW(TAG, "No options or timer number not configured");
    return;
  }
  const auto &options = this->traits.get_options();
  for (size_t i = 0; i < options.size(); ++i) {
    if (options[i] == value) {
      ESP_LOGD(TAG, "Setting timer index: %d", (int)i);
      this->timer_number_->make_call().set_value(static_cast<float>(i)).perform();
      this->publish_state(value);
      return;
    }
  }
  ESP_LOGW(TAG, "Unknown select option: %s", value.c_str());
}

}  // namespace genvex
}  // namespace esphome
