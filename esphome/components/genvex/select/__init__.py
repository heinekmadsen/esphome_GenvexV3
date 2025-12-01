import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import select, number
from .. import Genvex

CONF_SPEED_NUMBER = "speed_number_id"
CONF_TIMER_NUMBER = "timer_number_id"

ns = cg.esphome_ns.namespace("genvex")
GenvexSpeedSelect = ns.class_("GenvexSpeedSelect", select.Select, cg.Component)

CONFIG_SCHEMA = select.select_schema(GenvexSpeedSelect).extend({
    cv.GenerateID(): cv.declare_id(GenvexSpeedSelect),
    cv.Optional(CONF_SPEED_NUMBER): cv.use_id(number.Number),
    cv.Optional(CONF_TIMER_NUMBER): cv.use_id(number.Number),
    cv.Required("options"): cv.ensure_list(cv.string),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[cv.CONF_ID])
    yield cg.register_component(var, config)
    # register_select requires the full config and options explicitly
    yield select.register_select(var, config, options=config["options"]) 

    # Validate exactly one of speed or timer provided
    has_speed = CONF_SPEED_NUMBER in config
    has_timer = CONF_TIMER_NUMBER in config
    if has_speed == has_timer:
        raise cv.Invalid("Provide exactly one of speed_number_id or timer_number_id")

    if has_speed:
        speed_num = yield cg.get_variable(config[CONF_SPEED_NUMBER])
        cg.add(var.set_speed_number(speed_num))
    else:
        timer_num = yield cg.get_variable(config[CONF_TIMER_NUMBER])
        cg.add(var.set_timer_number(timer_num))

# Unified select: handled via to_code above (speed or timer)
