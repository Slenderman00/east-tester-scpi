import argparse
from eastTester import eastTester


def main():
    parser = argparse.ArgumentParser(description="Control east tester loads")

    parser.add_argument("-c", "--channel", type=int, required=True, help="Channel")
    parser.add_argument("-r", "--resistance", type=int, required=True, help="Resistance")

    args = parser.parse_args()

    t1 = eastTester()
    print(t1.system_beep())
    print(t1.set_channel(args.channel))
    print(t1.ch_mode('CR'))
    print(t1.resi_cr(args.resistance))
    print(t1.ch_switch('ON'))


if __name__ == '__main__':
    main()
