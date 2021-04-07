import unittest

from project.hardware.hardware import Hardware

from project.software.express_software import ExpressSoftware



class HardwareTest(unittest.TestCase):
    def setUp(self):
        self.hardware = Hardware('Hardware 1', 'Heavy', 500, 500)

    def test_attributes(self):
        self.assertEqual('Hardware 1', self.hardware.name)
        self.assertEqual('Heavy', self.hardware.type)
        self.assertEqual(500, self.hardware.memory)
        self.assertEqual(500, self.hardware.capacity)
        self.assertEqual([], self.hardware.software_components)

    def test_install__expect_success(self):
        software = ExpressSoftware('Express', 200, 100)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))

    def test_install__expect_raise__exception(self):
        software = ExpressSoftware('Express', 300, 300)
        with self.assertRaises(Exception) as ex:
            self.hardware.install(software)
        self.assertEqual('Software cannot be installed', str(ex.exception))

    def test_uninstall__when_software_in_components__expect_to_uninstall_it(self):
        software = ExpressSoftware('Express', 200, 100)
        self.hardware.install(software)
        self.assertEqual(1, len(self.hardware.software_components))
        self.hardware.uninstall(software)
        self.assertEqual([], self.hardware.software_components)


if __name__ == '__main__':
    unittest.main()
