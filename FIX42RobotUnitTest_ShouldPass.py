import unittest
import simplefix
import time


class FIXRobotUnitTest(unittest.TestCase):
    def setUp(self):
        self.client = simplefix.FixMessage()
        self.exch = simplefix.FixMessage()

    def clearMessageStore(self):
        # Implement a method to clear message store if needed
        pass

    def sendMessage(self, message):
        # Simulate sending a message
        print(f"Sending message: {message.encode()}")
        return message

    def receiveMessage(self, message):
        # Simulate receiving a message
        print(f"Receiving message: {message.encode()}")
        return message

    def test_NewOrderSingleFilled_AsNames_ShouldPass(self):
        self.clearMessageStore()
        time.sleep(1)

        # Create and send NewOrderSingle message
        new_order = simplefix.FixMessage()
        new_order.append_pair(8, "FIX.4.2")
        new_order.append_pair(35, "D")
        new_order.append_pair(49, "CLIENT")
        new_order.append_pair(56, "EXECUTOR")
        new_order.append_utc_timestamp(52)
        new_order.append_pair(11, "123")
        new_order.append_pair(21, "1")
        new_order.append_pair(55, "IBM")
        new_order.append_pair(54, "1")
        new_order.append_pair(38, "100")
        new_order.append_pair(40, "2")
        new_order.append_pair(44, "10.50")
        new_order.append_pair(59, "0")

        returnMessageInitiator = self.sendMessage(new_order)
        if returnMessageInitiator:
            self.assertEqual(returnMessageInitiator.get(35), b"D")

        time.sleep(1)
        returnMessageAcceptor = self.receiveMessage(new_order)
        if returnMessageAcceptor:
            self.assertEqual(returnMessageAcceptor.get(35), b"D")

        time.sleep(1)

        # Create and send ExecutionReportAck message
        exec_report_ack = simplefix.FixMessage()
        exec_report_ack.append_pair(8, "FIX.4.2")
        exec_report_ack.append_pair(35, "8")
        exec_report_ack.append_pair(49, "EXECUTOR")
        exec_report_ack.append_pair(56, "CLIENT")
        exec_report_ack.append_utc_timestamp(52)
        exec_report_ack.append_pair(11, "123")
        exec_report_ack.append_pair(37, "456")
        exec_report_ack.append_pair(17, "789")
        exec_report_ack.append_pair(20, "0")
        exec_report_ack.append_pair(150, "0")
        exec_report_ack.append_pair(39, "0")
        exec_report_ack.append_pair(55, "IBM")
        exec_report_ack.append_pair(38, "100")
        exec_report_ack.append_pair(54, "1")
        exec_report_ack.append_pair(44, "10.50")
        exec_report_ack.append_pair(151, "100")
        exec_report_ack.append_pair(14, "0")
        exec_report_ack.append_pair(6, "0.0")

        returnMessageAcceptor = self.sendMessage(exec_report_ack)
        if returnMessageAcceptor:
            self.assertEqual(returnMessageAcceptor.get(35), b"8")

        time.sleep(1)
        returnMessageInitiator = self.receiveMessage(exec_report_ack)
        if returnMessageInitiator:
            self.assertEqual(returnMessageInitiator.get(35), b"8")

        time.sleep(1)

        # Create and send ExecutionReportFill message
        exec_report_fill = simplefix.FixMessage()
        exec_report_fill.append_pair(8, "FIX.4.2")
        exec_report_fill.append_pair(35, "8")
        exec_report_fill.append_pair(49, "EXECUTOR")
        exec_report_fill.append_pair(56, "CLIENT")
        exec_report_fill.append_utc_timestamp(52)
        exec_report_fill.append_pair(11, "123")
        exec_report_fill.append_pair(37, "456")
        exec_report_fill.append_pair(17, "789")
        exec_report_fill.append_pair(20, "0")
        exec_report_fill.append_pair(150, "2")
        exec_report_fill.append_pair(39, "2")
        exec_report_fill.append_pair(55, "IBM")
        exec_report_fill.append_pair(38, "100")
        exec_report_fill.append_pair(54, "1")
        exec_report_fill.append_pair(44, "10.50")
        exec_report_fill.append_pair(32, "100")
        exec_report_fill.append_pair(31, "10.50")
        exec_report_fill.append_pair(151, "0")
        exec_report_fill.append_pair(14, "100")
        exec_report_fill.append_pair(6, "10.50")

        returnMessageAcceptor = self.sendMessage(exec_report_fill)
        if returnMessageAcceptor:
            self.assertEqual(returnMessageAcceptor.get(35), b"8")

        time.sleep(1)
        returnMessageInitiator = self.receiveMessage(exec_report_fill)
        if returnMessageInitiator:
            self.assertEqual(returnMessageInitiator.get(35), b"8")

        time.sleep(1)

        self.logDumpMessageStore()

    def logDumpMessageStore(self):
        # Implement a method to log dump message store if needed
        pass


if __name__ == "__main__":
    unittest.main()
