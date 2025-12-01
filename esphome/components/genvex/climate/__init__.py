import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import climate, sensor, number
from .. import Genvex
from esphome.const import CONF_ID

CONF_TARGET_TEMP = "target_temp_number_id"
CONF_CURRENT_TEMP = "current_temp_sensor_id"
CONF_FAN_SPEED = "fan_speed_number_id"

ns = cg.esphome_ns.namespace("genvex")
GenvexClimate = ns.class_("GenvexClimate", climate.Climate, cg.Component)

CONFIG_SCHEMA = climate.climate_schema(GenvexClimate).extend({
    cv.GenerateID(): cv.declare_id(GenvexClimate),
    cv.Required(CONF_TARGET_TEMP): cv.use_id(number.Number),
    cv.Required(CONF_CURRENT_TEMP): cv.use_id(sensor.Sensor),
    cv.Optional(CONF_FAN_SPEED): cv.use_id(number.Number),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    yield climate.register_climate(var, config)

    number_set_temp = yield cg.get_variable(config[CONF_TARGET_TEMP])
    cg.add(var.set_temp_setpoint_number(number_set_temp))

    sens_current_temp = yield cg.get_variable(config[CONF_CURRENT_TEMP])
    cg.add(var.set_current_temp_sensor(sens_current_temp))

    if CONF_FAN_SPEED in config:
        fan_speed_num = yield cg.get_variable(config[CONF_FAN_SPEED])
        cg.add(var.set_fan_speed_number(fan_speed_num))
