################################
#
# Enums
#
################################
from enum import Enum
import utils as u


u.clear()

# non-standard at least to java or C terms,
# python enums are classes
class TrafficLight(Enum):
	GREEN = 1
	YELLOW = 2
	RED = 4


u.banner("can access values as .name or .value params")
##############################

# can access values as name or value params
print(TrafficLight.GREEN.name)
print(TrafficLight.GREEN.value)


u.banner("or indexed...")
##############################

print(TrafficLight(2).name)
print(TrafficLight(2).value)
