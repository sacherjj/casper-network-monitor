from dataclasses import dataclass


@dataclass()
class Network:
    """
    Holds data for a casper network
    """
    name: str
    ips: list
    protocol_url: str


_casper_ips = ["178.238.235.196",
               "47.242.53.164",
               "135.181.216.81",
               "168.119.137.143",
               "54.39.129.78",
               "135.181.165.110",
               "134.209.16.172",
               "46.4.91.24",
               "134.122.45.61",
               "99.81.225.72",
               "47.251.14.254",
               "207.246.114.236",
               "101.36.120.117",
               "3.17.72.47",
               "63.33.251.206",
               "3.14.161.135",
               "18.188.152.102",
               "34.122.31.70",
               "54.215.53.35",
               "54.39.133.124",
               "51.89.232.234",
               "135.181.116.109",
               "157.90.131.121",
               "157.90.131.49",
               "178.33.239.236",
               "46.101.61.107",
               "31.7.207.16",
               "35.169.205.205",
               "82.95.0.200",
               "139.162.132.144",
               "148.251.190.103",
               "148.251.135.60",
               "134.209.110.11",
               "98.149.220.243",
               "1.15.171.36",
               "62.171.135.101",
               "168.119.209.31",
               "18.219.70.138",
               "157.90.106.242",
               "45.76.251.225",
               "209.145.60.74",
               "47.88.87.63",
               "135.181.134.57",
               "88.99.95.7",
               "188.40.83.254",
               "54.151.24.120",
               "165.22.252.48",
               "168.119.69.6",
               "3.12.207.193",
               "167.172.32.44",
               "54.39.129.79",
               "134.209.243.124",
               "18.191.239.36",
               "3.225.191.9",
               "13.58.71.180",
               "94.130.107.198",
               "18.188.103.230",
               "3.142.224.108",
               "35.152.42.229",
               "62.171.177.179",
               "52.207.122.179",
               "54.180.220.20",
               "62.171.172.72",
               "54.252.66.23",
               "206.189.47.102",
               "3.221.194.62"]

_casper_test_ips = ["3.208.91.63", "35.169.197.193"]

_integration_test_ips = ["3.140.179.157", "3.138.177.248", "3.143.158.19", "3.139.47.90", "18.219.25.234"]

NETWORKS = [Network(name="casper",
                    ips=_casper_ips,
                    protocol_url="http://genesis.casperlabs.io"),
            Network(name="casper-test",
                    ips=_casper_test_ips,
                    protocol_url="https://casper-genesis.make.services"),
            Network(name="integration-test",
                    ips=_integration_test_ips,
                    protocol_url="http://genesis.casperlabs.io")]
