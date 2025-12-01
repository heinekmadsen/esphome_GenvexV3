#include "genvex.h"
#include "esphome/core/log.h"

namespace esphome {
namespace genvex {

static const char *TAG = "genvex";

void Genvex::dump_config() {
  ESP_LOGCONFIG(TAG, "Genvex root component");
}

}  // namespace genvex
}  // namespace esphome
