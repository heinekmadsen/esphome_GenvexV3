import esphome.codegen as cg
import esphome.config_validation as cv

from esphome.const import CONF_ID

# Root component namespace and class
GENVEX_NS = cg.esphome_ns.namespace("genvex")
Genvex = GENVEX_NS.class_("Genvex", cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Genvex),
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
