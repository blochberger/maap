import unittest

from bundle.bundle import Bundle
from bundle.types import BundleType


class TestFramework(unittest.TestCase):
    """Tests for the `Framework` class"""
    def setUp(self):
        self.framework = Bundle.make("/System/Library/Frameworks/DVDPlayback.framework")

    def test_bundle_type(self):
        self.assertEqual(self.framework.bundle_type, BundleType.FRAMEWORK)

    def test_paths(self):
        # Since we don't know which MAS app is chosen, only the system app is tested here.
        self.assertEqual(self.framework.executable_path(),
                         "/System/Library/Frameworks/DVDPlayback.framework/Versions/A/DVDPlayback")
        self.assertEqual(self.framework.info_dictionary_path(),
                         "/System/Library/Frameworks/DVDPlayback.framework/Versions/A/Resources/Info.plist")

    def test_linked_libraries(self):
        framework_bin = self.framework.executable()
        linked_libraries = framework_bin.linked_libraries()
        application_libraries = framework_bin.application_libraries()

        self.assertTrue(len(linked_libraries) == 23)
        self.assertTrue(len(application_libraries) == 0)