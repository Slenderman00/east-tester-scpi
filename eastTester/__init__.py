import serial
import sys

# https://www.tonyplaza.nl/download/YT0394/ET54ET53_SCPI.pdf


class eastTester:
    def __init__(self, interface='/dev/ttyUSB0', baudrate=115200, timeout=1):
        self.interface = interface
        self.ser = serial.Serial(self.interface)
        self.ser.baudrate = baudrate
        self.ser.timeout = timeout
        self.channel = ''

    def write(self, path, command='', channel=True):
        if channel:
            _path = path.split(':')
            path = f'{_path[0]}{self.channel}:{_path[1]}'
        data = f'{path} {command}'
        data = data.replace(' ?', '?')
        self.ser.write(f'{data}\n'.encode())
        # print(data)
        data = self.ser.read(1000000)
        _data = str(data)
        sys.stdout.flush()
        return _data

    def set_channel(self, channel):
        self.channel = channel

    def idn(self):
        return self.write('*idn?', channel=False)

    def trg(self):
        return self.write('*trg', channel=False)

    def system_version(self):
        return self.write('SYST:VERS', channel=False)

    def system_beep(self):
        return self.write('SYST:BEEP', channel=False)

    def system_local(self):
        return self.write('SYST:LOCA', channel=False)

    def load_trigger(self, trigger):
        """Selects trigger for the current channel

        Args:
            trigger (string): MAN, EXT or TRG

        Returns:
            byte[]: result
        """
        return self.write('LOAD:TRIG', trigger)

    def load_voltage_range(self, range):
        """Selects voltage range for the current channel

        Args:
            range (string): HIGH or Low

        Returns:
            byte[]: result HIGH or LOW
        """
        return self.write('LOAD:VRAN', range)

    def load_current_range(self, range):
        """Selects current range for the current channel

        Args:
            range (string): HIGH or Low

        Returns:
            byte[]: result HIGH or LOW
        """
        return self.write('LOAD:CRAN', range)

    def load_abnormal(self):
        """Query whether the current load is abnormal

        Returns:
            byte[]: result NONE, OV, OC, THE OP, OT, LRV, THE UN and FAIL
        """
        return self.write('LOAD:ABNO')

    def quality_test(self, status):
        """Set the status of the quality test

        Args:
            status (string): ON or OFF

        Returns:
            byte[]: result ON or OFF
        """
        return self.write('QUAL:TEST', status)

    def quality_out(self):
        """Checks whether the quality test passed

        Returns:
            byte[]: NONE, PASS or FAIL
        """
        return self.write('QUAL:OUT')

    def quality_voltage_high(self, voltage):
        """Set the upper limit voltage value, can query the current upper
        limit voltage value

        Args:
            voltage (integer): The upper limit of the voltage

        Returns:
            byte[]: The upper limit of the voltage
        """
        return self.write('QUAL:VHIG', voltage)

    def quality_voltage_low(self, voltage):
        """Set the lower limit voltage value, can query the current upper
        limit voltage value

        Args:
            voltage (integer): The lower limit of the voltage

        Returns:
            byte[]: The lower limit of the voltage
        """
        return self.write('QUAL:VLOW', voltage)

    def quality_current_high(self, current):
        """Set the upper limit power value to query the
        current upper limit power value

        Args:
            current (integer): The upper limit of the current

        Returns:
            byte[]: The upper limit of the current
        """
        return self.write('QUAL:CHIG', current)

    def quality_current_low(self, current):
        """Set the lower limit current value, can query the current upper
        limit voltage value

        Args:
            current (integer): The lower limit of the current

        Returns:
            byte[]: The lower limit of the current
        """
        return self.write('QUAL:CLOW', current)

    def quality_power_high(self, power):
        """Set the upper limit power value to query
        the current upper limit power value

        Args:
            power (integer): The upper limit of the power

        Returns:
            byte[]: The upper limit of the power
        """
        return self.write('QUAL:PHIG', power)

    def quality_power_low(self, power):
        """Set the lower limit power value to query
        the current lower limit power value

        Args:
            power (integer): The lower limit of the power

        Returns:
            byte[]: The lower limit of the power
        """
        return self.write('QUAL:PLOW', power)

    # Not implementing SYSSet:STARt

    # Not implementing SYSSet:LANGuage

    # Not implementing COMMand:BAUDrate

    def volt_on(self, voltage):
        return self.write('VOLT:ON', voltage)

    def volt_off(self, voltage):
        return self.write('VOLT:OFF', voltage)

    def volt_max(self, voltage):
        return self.write('VOLT:VMAX', voltage)

    def volt_cv(self, voltage):
        return self.write('VOLT:CV', voltage)

    def volt_cccv(self, voltage):
        return self.write('VOLT:CCCV', voltage)

    def volt_crcv(self, voltage):
        return self.write('VOLT:CRCV', voltage)

    def volt_ta(self, voltage):
        return self.write('VOLT:TA', voltage)

    def volt_tb(self, voltage):
        return self.write('VOLT:CB', voltage)

    def volt_led(self, voltage):
        return self.write('VOLT:LED', voltage)

    def volt_bcr(self, voltage):
        return self.write('VOLT:BCR', voltage)

    def volt_bcc1(self, voltage):
        return self.write('VOLT:BCC1', voltage)

    def volt_bcc2(self, voltage):
        return self.write('VOLT:BCC2', voltage)

    def volt_bcc3(self, voltage):
        return self.write('VOLT:BCC3', voltage)

    def volt_start(self, voltage):
        return self.write('VOLT:STAR', voltage)

    def volt_end(self, voltage):
        return self.write('VOLT:END', voltage)

    def volt_step(self, voltage):
        return self.write('VOLT:STEP', voltage)

    def volt_vth(self, voltage):
        return self.write('VOLT:VTH', voltage)

    def volt_vmin(self, voltage):
        return self.write('VOLT:VMIN', voltage)

    def volt_low(self, voltage):
        return self.write('VOLT:LOW', voltage)

    def volt_high(self, voltage):
        return self.write('VOLT:HIGH', voltage)

    def current_on(self, current):
        return self.write('CURR:ON', current)

    def current_off(self, current):
        return self.write('CURR:OFF', current)

    def current_max(self, current):
        return self.write('CURR:VMAX', current)

    def current_cv(self, current):
        return self.write('CURR:CV', current)

    def current_cccv(self, current):
        return self.write('CURR:CCCV', current)

    def current_crcv(self, current):
        return self.write('CURR:CRCV', current)

    def current_ta(self, current):
        return self.write('CURR:TA', current)

    def current_tb(self, current):
        return self.write('CURR:CB', current)

    def current_led(self, current):
        return self.write('CURR:LED', current)

    def current_bcr(self, current):
        return self.write('CURR:BCR', current)

    def current_bcc1(self, current):
        return self.write('CURR:BCC1', current)

    def current_bcc2(self, current):
        return self.write('CURR:BCC2', current)

    def current_bcc3(self, current):
        return self.write('CURR:BCC3', current)

    def current_start(self, current):
        return self.write('CURR:STAR', current)

    def current_end(self, current):
        return self.write('CURR:END', current)

    def current_step(self, current):
        return self.write('CURR:STEP', current)

    def current_vth(self, current):
        return self.write('CURR:VTH', current)

    def current_vmin(self, current):
        return self.write('CURR:VMIN', current)

    def current_low(self, current):
        return self.write('CURR:LOW', current)

    def current_high(self, current):
        return self.write('CURR:HIGH', current)
    
    def resi_cr(self, resistance):
        return self.write('RESI:CR', resistance)

    def power_on(self, power):
        return self.write('POWE:ON', power)

    def power_off(self, power):
        return self.write('POWE:OFF', power)

    def power_max(self, power):
        return self.write('POWE:PMAX', power)

    def power_cv(self, power):
        return self.write('POWE:CV', power)

    def power_cccv(self, power):
        return self.write('POWE:CCCV', power)

    def power_crcv(self, power):
        return self.write('POWE:CRCV', power)

    def power_ta(self, power):
        return self.write('POWE:TA', power)

    def power_tb(self, power):
        return self.write('POWE:CB', power)

    def power_led(self, power):
        return self.write('POWE:LED', power)

    def power_bcr(self, power):
        return self.write('POWE:BCR', power)

    def power_bcc1(self, power):
        return self.write('POWE:BCC1', power)

    def power_bcc2(self, power):
        return self.write('POWE:BCC2', power)

    def power_bcc3(self, power):
        return self.write('POWE:BCC3', power)

    def power_start(self, power):
        return self.write('POWE:STAR', power)

    def power_end(self, power):
        return self.write('POWE:END', power)

    def power_step(self, power):
        return self.write('POWE:STEP', power)

    def power_vth(self, power):
        return self.write('POWE:VTH', power)

    def power_vmin(self, power):
        return self.write('POWE:VMIN', power)

    def power_low(self, power):
        return self.write('POWE:LOW', power)

    def power_high(self, power):
        return self.write('POWE:HIGH', power)

    def time_off_delay(self, time):
        return self.write('TIME:OFFD', time)

    def time_wa(self, time):
        return self.write('TIME:WA', time)

    def time_wb(self, time):
        return self.write('TIME:WB', time)

    def time_step(self, time):
        return self.write('TIME:STEP', time)

    def led_coefficient(self, coefficient):
        return self.write('LED:COEFF', coefficient)

    def tran_state(self, state):
        return self.write('TRAN:STAT', state)

    def tran_mode(self, mode):
        return self.write('TRAN:MODE', mode)

    def batt_mode(self, mode):
        return self.write('BATT:MODE', mode)

    def batt_capacity(self, capacity):
        return self.write('BATT:CAPA', capacity)

    def scan_type(self, type):
        return self.write('SCAN:TYPE', type)

    def scan_thtype(self, type):
        return self.write('SCAN:THTY', type)

    def scan_compare(self, compare):
        return self.write('SCAN:COMP', compare)

    def list_loop(self, status):
        return self.write('LIST:LOOP', status)

    def list_mode(self, mode):
        return self.write('LIST:MODE', mode)

    def list_num(self, num):
        return self.write('LIST:NUM', num)

    def list_parameter(self, parameters):
        return self.write('LIST:PARA', parameters)

    def list_out(self, start, end):
        return self.write('LIST:OUT', f'? {start}, {end}')

    def ch_mode(self, mode):
        return self.write('CH:MODE', mode)

    def ch_switch(self, status):
        return self.write('CH:SW', status)

    # File subsystem is not implemented

    def meas_current(self):
        return self.write('MEAS:CURR', '?')

    def meas_voltage(self):
        return self.write('MEAS:VOLT', '?')

    def meas_power(self):
        return self.write('MEAS:POW', '?')

    def meas_resistance(self):
        return self.write('MEAS:RESI', '?')

    def meas_all(self):
        return self.write('MEAS:ALL', '?')

    def self_fan(self):
        return self.write('SELF:FAN', '?', channel=False)
