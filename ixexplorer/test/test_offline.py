"""
IxExplorer package tests that can run in offline mode.

@author yoram@ignissoft.com
"""

from ixexplorer.test.test_base import IxeTestBase


class IxExplorerTestBase(IxeTestBase):

    def testLoadConfig(self):

        cfg1 = 'c:/configs/test_config_1.prt'
        cfg2 = 'c:/configs/test_config_2.prt'
        self._load_config(cfg1, cfg2)

        assert(len(self.ports) == 2)
        assert(len(self.ports[self.port1].streams) == 2)
        assert(len(self.ports[self.port2].streams) == 2)

        assert(self.ports[self.port1].streams[1].da == '22:22:22:22:22:11')
        assert(self.ports[self.port1].streams[1].sa == '11:11:11:11:11:11')
        assert(self.ports[self.port1].streams[2].da == '22:22:22:22:22:22')
        assert(self.ports[self.port1].streams[2].sa == '11:11:11:11:11:22')

        self.ports[self.port1].streams[1].da = '33:33:33:33:33:33'
        self.ports[self.port1].streams[1].sa = '44:44:44:44:44:44'

        assert(self.ports[self.port1].streams[1].da == '33:33:33:33:33:33')
        assert(self.ports[self.port1].streams[1].sa == '44:44:44:44:44:44')
        assert(self.ports[self.port1].streams[2].da == '22:22:22:22:22:22')
        assert(self.ports[self.port1].streams[2].sa == '11:11:11:11:11:22')

    def testBuildConfig(self):
        self._reserve_ports()

        self.ports[self.port1].add_stream()
        self.ports[self.port1].streams[1].da = "22:22:22:22:22:11"
        self.ports[self.port1].streams[1].sa = "11:11:11:11:11:11"
        self.ports[self.port1].streams[1].protocol.ethernet_type = 'ethernetII'
        self.ports[self.port1].streams[1].protocol.name = 'ipV4'
        self.ports[self.port1].streams[1].ip.dest_ip_addr = '1.1.2.1'
        self.ports[self.port1].add_stream()
        self.ports[self.port1].streams[2].da = "22:22:22:22:22:22"
        self.ports[self.port1].streams[2].sa = "11:11:11:11:11:22"
        self.ports[self.port1].write()

        assert(self.ports[self.port1].streams[1].da == '22:22:22:22:22:11')
        assert(self.ports[self.port1].streams[1].sa == '11:11:11:11:11:11')
        assert(self.ports[self.port1].streams[2].da == '22:22:22:22:22:22')
        assert(self.ports[self.port1].streams[2].sa == '11:11:11:11:11:22')

        self.ports[self.port2].add_stream()
        self.ports[self.port2].streams[1].da = "11:11:11:11:11:11"
        self.ports[self.port2].streams[1].sa = "22:22:22:22:22:11"
        self.ports[self.port2].add_stream()
        self.ports[self.port2].streams[2].da = "11:11:11:11:11:22"
        self.ports[self.port2].streams[2].sa = "22:22:22:22:22:22"
        self.ports[self.port2].write()

        assert(self.ports[self.port1].streams[1].da == '22:22:22:22:22:11')
        assert(self.ports[self.port1].streams[1].sa == '11:11:11:11:11:11')
        assert(self.ports[self.port1].streams[2].da == '22:22:22:22:22:22')
        assert(self.ports[self.port1].streams[2].sa == '11:11:11:11:11:22')