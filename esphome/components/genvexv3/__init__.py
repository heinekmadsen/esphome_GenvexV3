import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID

genvexv3_ns = cg.esphome_ns.namespace('genvexv3')
Genvexv3 = genvexv3_ns.class_('Genvexv3', cg.Component)

CONF_GENVEXV3_ID = 'genvexv3_id'

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(Genvexv3),   
})

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config) 
