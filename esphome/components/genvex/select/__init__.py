import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select, number
from .. import Genvex

CONF_SPEED_NUMBER = "speed_number_id"
CONF_TIMER_NUMBER = "timer_number_id"

ns = cg.esphome_ns.namespace("genvex")
GenvexSpeedSelect = ns.class_("GenvexSpeedSelect", select.Select, cg.Component)
GenvexTimerSelect = ns.class_("GenvexTimerSelect", select.Select, cg.Component)

CONFIG_SCHEMA = select.select_schema(GenvexSpeedSelect).extend({
    cv.GenerateID(): cv.declare_id(GenvexSpeedSelect),
    cv.GenerateID("genvex_id"): cv.use_id(Genvex),
    cv.Required(CONF_SPEED_NUMBER): cv.use_id(number.Number),
    cv.Required("options"): cv.ensure_list(cv.string),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[cv.CONF_ID])
    yield cg.register_component(var, config)
    yield select.register_select(var, config)

    speed_num = yield cg.get_variable(config[CONF_SPEED_NUMBER])
    cg.add(var.set_speed_number(speed_num))

# Separate schema for timer select
TIMER_CONFIG_SCHEMA = select.select_schema(GenvexTimerSelect).extend({
    cv.GenerateID(): cv.declare_id(GenvexTimerSelect),
    cv.GenerateID("genvex_id"): cv.use_id(Genvex),
    cv.Required(CONF_TIMER_NUMBER): cv.use_id(number.Number),
    cv.Required("options"): cv.ensure_list(cv.string),
}).extend(cv.COMPONENT_SCHEMA)

def timer_to_code(config):
    var = cg.new_Pvariable(config[cv.CONF_ID])
    yield cg.register_component(var, config)
    yield select.register_select(var, config)

    timer_num = yield cg.get_variable(config[CONF_TIMER_NUMBER])
    cg.add(var.set_timer_number(timer_num))
