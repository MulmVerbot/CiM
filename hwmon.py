import tkinter as tk
from tkinter import ttk
import platform
import psutil


def get_system_metrics():
    metrics = {}

    metrics['System'] = {
        'Platform': platform.system(),
        'Platform Version': platform.version(),
        'Platform Release': platform.release(),
        'Architecture': platform.architecture(),
        'Machine': platform.machine(),
        'Processor': platform.processor(),
    }

    metrics['CPU'] = {
        'Cores': psutil.cpu_count(logical=False),
        'Logical CPUs': psutil.cpu_count(logical=True),
        'CPU Frequency': psutil.cpu_freq().current if psutil.cpu_freq() else 'N/A',
        'CPU Usage (%)': psutil.cpu_percent(interval=0),
    }

    vm = psutil.virtual_memory()
    metrics['Memory'] = {
        'Total Memory': f"{vm.total / (1024 ** 3):.2f} GB",
        'Available Memory': f"{vm.available / (1024 ** 3):.2f} GB",
        'Used Memory': f"{vm.used / (1024 ** 3):.2f} GB",
        'Memory Usage (%)': vm.percent,
    }

    disk = psutil.disk_usage('/')
    metrics['Disk'] = {
        'Total Disk Space': f"{disk.total / (1024 ** 3):.2f} GB",
        'Used Disk Space': f"{disk.used / (1024 ** 3):.2f} GB",
        'Free Disk Space': f"{disk.free / (1024 ** 3):.2f} GB",
        'Disk Usage (%)': disk.percent,
    }

    net = psutil.net_if_addrs()
    metrics['Network'] = {
        'Network Interfaces': list(net.keys()),
    }

    return metrics


def display_metrics_in_gui(metrics):
    def update_metrics():
        updated_metrics = get_system_metrics()

        for category, data in updated_metrics.items():
            for key, value in data.items():
                value_str = value if isinstance(value, str) else str(value)
                labels[category][key]['text'] = f"{key}: {value_str}"

        # Funktion erneut nach 1 Sekunde ausführen
        root.after(100, update_metrics)

    root = tk.Tk()
    root.title("Systeminfos")
    header = tk.Label(root, text="Systeminfos", font=("Helvetica", 16, "bold"))
    header.pack(pady=10)

    main_frame = ttk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(main_frame)
    scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)


    labels = {}
    for category, data in metrics.items():
        category_label = tk.Label(scrollable_frame, text=f"{category}:", font=("Helvetica", 14, "bold"))
        category_label.pack(anchor="w", pady=(10, 0))

        labels[category] = {}
        for key, value in data.items():
            value_str = value if isinstance(value, str) else str(value)
            data_label = tk.Label(scrollable_frame, text=f"  {key}: {value_str}", font=("Helvetica", 12))
            data_label.pack(anchor="w")
            labels[category][key] = data_label

    # Erste Aktualisierung starten
    root.after(1000, update_metrics)

    root.mainloop()


if __name__ == "__main__":
    metrics = get_system_metrics()
    display_metrics_in_gui(metrics)
