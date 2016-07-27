from burrowbeat import TestCase


"""
Contains tests for consumer lag.
"""


class Test(TestCase):
    def test_consumer_stats(self):
        """
        Checks that consumer info is found in the output
        and its fields have the expected types.
        """
        self.render_config_template()
        burrowbeat = self.start_burrowbeat()
        self.wait_until(lambda: self.output_has(lines=1))
        burrowbeat.kill_and_wait()

        output = self.read_output()[0]

        for key in [
            "consumer_group_name",
        ]:
            assert type(output[key].encode('ascii','ignore')) is str

        for key in [
            "lag",
            "offset",
        ]:
            assert type(output[key]) is int

