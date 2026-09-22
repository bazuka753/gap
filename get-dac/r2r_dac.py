import RPi.GPIO as gpio

class r2r_dac:
    def _init_(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        gpio.setmode(gpio.BCM)
        gpio.setup(self.gpio_bits, gpio.OUT, initial = 0)

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"напряжение выходит за динамический диапазон ЦАП (0.0 - {dynamic_range:.2f} В)")
            return 0
        return int(voltage / dynamic_range * 255)

    def set_number(self, number):
        return [int(element) for element in bin(number)[2:].zfill(8)]


def deinit(self):
    gpio.output(self.gpio_bits, 0)
    gpio.cleanup()

id _name == 'main'