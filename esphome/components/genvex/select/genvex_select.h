#pragma once

#include "esphome/core/component.h"
#include "esphome/components/select/select.h"
#include "esphome/components/number/number.h"

namespace esphome {
namespace genvex {

class GenvexSpeedSelect : public select::Select, public Component {
public:
  GenvexSpeedSelect() {}

  void setup() override {}
  void dump_config() override;

  void set_speed_number(number::Number *number) { this->speed_number_ = number; }
  void set_timer_number(number::Number *number) { this->timer_number_ = number; }

protected:
  void control(const std::string &value) override;

  number::Number *speed_number_{nullptr};
  number::Number *timer_number_{nullptr};
};

}  // namespace genvex
}  // namespace esphome
