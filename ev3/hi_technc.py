import sensor, struct, ctypes
from rawdevice import lms2012

class HiTechncCompass(sensor.IICSensor):
	def __init__(self, port, address):
		super(HiTechncCompass, self).__init__(port, address)
		
	def get_angle(self):
		sensor_data = self.read(0x42, 2)
		return (ctypes.c_uint8(sensor_data[0]).value * 2 + ctypes.c_uint8(sensor_data[1]).value)