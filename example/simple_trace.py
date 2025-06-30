# -*- coding: utf-8 -*-
import os

import perfetto_extras as pftrace

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    # Create a trace object
    trace = pftrace.Trace()

    # Counter events
    counter_events = trace.create_process_track("CounterDemo", "Counter")
    counter_events.add_counter_event(
        name="Counter",
        ts=1000,
        args={"cat": "2", "dog": "4"}
    )
    counter_events.add_counter_event(
        name="Counter",
        ts=2000,
        args={"cat": "3", "dog": "5"}
    )
    counter_events.add_counter_event(
        name="Counter",
        ts=3000,
        args={"cat": "4", "dog": "6"}
    )

    # Complete events
    complete_events = trace.create_process_track("CompleteDemo", "Complete")
    complete_thread1 = complete_events.create_thread_track("CompleteThread", "Complete")
    complete_thread1.add_complete_event(
        name="Complete",
        ts=1000,
        duration_us=1000,
        args={"name": "Complete1", "value": 100}
    )
    complete_thread1.add_complete_event(
        name="Complete",
        ts=3000,
        duration_us=3000,
        args={"name": "Complete3", "value": 300}
    )
    complete_thread2 = complete_events.create_thread_track("CompleteThread", "Complete")
    complete_thread2.add_complete_event(
        name="Complete",
        ts=2000,
        duration_us=2000,
        args={"name": "Complete2", "value": 200}
    )

    # Instant events
    instant_events = trace.create_process_track("InstantDemo", "ProcessInstant")
    instant_thread1 = instant_events.create_thread_track("InstantThread", "ThreadInstant1")
    instant_thread1.add_instant_event(
        name="Instant",
        ts=1000,
        args={"name": "Instant1", "value": 100}
    )
    
    instant_thread2 = instant_events.create_thread_track("InstantThread", "ThreadInstant2")
    instant_thread2.add_instant_event(
        name="Instant",
        ts=2000,
        args={"name": "Instant2", "value": 200}
    )

    # Save the trace to a file
    trace_file = os.path.join(CURRENT_DIR, "simple_trace.json")
    trace.dump(
        indent=2,
        fp = open(trace_file, "w")
    )

    # Open the trace file
    pftrace.open_trace_in_browser(trace_file)