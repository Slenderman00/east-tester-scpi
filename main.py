from eastTester import eastTester

t1 = eastTester()

t1.set_channel(1)
print(t1.idn())
print(t1.system_beep())
print(t1.meas_all())
print(t1.self_fan())
print(t1.tran_state('CC'))