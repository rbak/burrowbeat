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
        self.wait_until(lambda: self.output_has(lines=2))
        burrowbeat.kill_and_wait()

        output = self.read_output()[0]

        for key in [
            "cluster",
            "group",
        ]:
            assert type(output[key].encode('ascii','ignore')) is str

        for key in [
            "total_lag",
            "total_partitions",
        ]:
            assert type(output[key]) is int

        output = self.read_output()[1]

        for key in [
            "cluster",
            "group",
            "topic.name"
        ]:
            assert type(output[key].encode('ascii','ignore')) is str

        for key in [
            "topic.lag",
            "topic.partitions",
            "topic.size",
        ]:
            assert type(output[key]) is int

