#pragma once

#include "esphome/core/component.h"
#include "esphome/components/select/select.h"
#include "esphome/components/number/number.h"

namespace esphome {
namespace genvex {

class GenvexTimerSelect : public select::Select, public Component {
public:
  GenvexTimerSelect() {}

  void setup() override {}
  void dump_config() override;

  void set_timer_number(number::Number *number) { this->timer_number_ = number; }

protected:
  void control(const std::string &value) override;

  number::Number *timer_number_{nullptr};
};

}  // namespace genvex
}  // namespace esphome
