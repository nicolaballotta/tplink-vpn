import tplink
import argparse

more_indent_formatter = lambda prog: argparse.RawTextHelpFormatter(prog, max_help_position=40)

parser = argparse.ArgumentParser(description='Enable/Disable VPN on TPLink routers',
                                 formatter_class=more_indent_formatter)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-on', action='store_true', default=False, help='enable VPN')
group.add_argument('-off', action='store_true', default=False, help='disable VPN')
parser.add_argument('-u', '--username', default='admin', help='TPLink router username (default: %(default)s)')
parser.add_argument('-p', '--password', default='admin', help='TPLink router password (default: %(default)s)')
parser.add_argument('-a', '--address', default='192.168.0.1', help='TPLink router address (default: %(default)s)')

if __name__ == '__main__':
    args = parser.parse_args()
    router = tplink.Tplink('http://' + args.address + '/webpages/login.html?t=1516775402233', args.username,
                           args.password)

    if args.on:
        router.vpn_on()
    elif args.off:
        router.vpn_off()
