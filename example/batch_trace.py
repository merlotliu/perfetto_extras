# -*- coding: utf-8 -*-
import os

import perfetto_extras as pftrace

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == "__main__":
    # 创建 Trace 对象
    t = pftrace.Trace()

    # 批量添加 counter 事件
    counter_timestamps = [1000, 2000, 3000]
    counter_values = [
        {"cat": 2, "dog": 4},
        {"cat": 3, "dog": 5},
        {"cat": 4, "dog": 6}
    ]
    t.add_batch_counter_events(
        process_name="CounterDemo",
        category="Counter",
        name_prefix="Counter",
        timestamps=counter_timestamps,
        values_list=counter_values
    )

    # 批量添加 instant 事件
    instant_timestamps = [1100, 2100, 3100]
    instant_args = [
        {"event": "A"},
        {"event": "B"},
        {"event": "C"}
    ]
    t.add_batch_instant_events(
        process_name="InstantDemo",
        process_category="InstantCat",
        thread_name="Thread-1",
        thread_category="ThreadCat",
        timestamps=instant_timestamps,
        args_list=instant_args
    )

    # 批量添加 complete 事件
    complete_timestamps = [1200, 2200, 3200]
    complete_durations = [50, 60, 70]
    complete_args = [
        {"task": "X"},
        {"task": "Y"},
        {"task": "Z"}
    ]
    t.add_batch_complete_events(
        process_name="CompleteDemo",
        process_category="CompleteCat",
        thread_name="Thread-2",
        thread_category="ThreadCat",
        timestamps=complete_timestamps,
        durations=complete_durations,
        args_list=complete_args
    )

    # 导出为 JSON
    with open(os.path.join(CURRENT_DIR, "batch_trace.json"), "w") as f:
        f.write(t.dumps(indent=2, ensure_ascii=False))

    pftrace.open_trace_in_browser(os.path.join(CURRENT_DIR, "batch_trace.json"))