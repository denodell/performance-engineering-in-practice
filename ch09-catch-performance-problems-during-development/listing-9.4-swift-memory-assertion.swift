#if DEBUG
import Darwin
func assertMemory(
    _ label: String,
    thresholdMB: Double = 20,
    block: () -> Void
) {
    let before = physFootprintMB()
    block()
    let deltaMB = physFootprintMB() - before
    if deltaMB > thresholdMB {
        print(
            "WARNING: \(label) increased memory by"
            + " \(String(format: "%.1f", deltaMB))MB"
            + " (threshold: \(String(format: "%.0f", thresholdMB))MB)"
        )
    }
}

private func physFootprintMB() -> Double {
    var info = task_vm_info_data_t()
    var count = mach_msg_type_number_t(
        MemoryLayout<task_vm_info_data_t>.size
    ) / 4
    task_info(
        mach_task_self_,
        task_flavor_t(TASK_VM_INFO),
        withUnsafeMutablePointer(to: &info) {
            $0.withMemoryRebound(
                to: integer_t.self, capacity: Int(count)
            ) { $0 }
        },
        &count
    )
    return Double(info.phys_footprint) / 1048576.0
}

#endif
