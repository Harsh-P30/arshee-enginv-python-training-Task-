import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QMessageBox, QComboBox, QFileDialog, QInputDialog
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.signal import butter, lfilter
from scipy.io import loadmat

# --- Frequency weighting ---
def butter_bandpass(lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a

def apply_frequency_weighting(data, fs, weighting='Wk'):
    if weighting == 'Wk':
        lowcut, highcut = 0.4, 100
    elif weighting == 'Wa':
        lowcut, highcut = 0.4, 100
    elif weighting == 'Wd':
        lowcut, highcut = 0.5, 80
    else:
        lowcut, highcut = 0.4, 100
    b, a = butter_bandpass(lowcut, highcut, fs)
    return lfilter(b, a, data)

def calculate_weighted_rms(data):
    return np.sqrt(np.mean(np.square(data)))

class VibrationEvaluator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ISO 2631-1 Vibration Evaluation")
        self.setGeometry(100, 100, 900, 600)

        self.data = None
        self.fs = None

        main_layout = QVBoxLayout()
        control_layout = QHBoxLayout()

        # Controls
        self.btn_load = QPushButton("Load .mat File")
        self.btn_load.clicked.connect(self.load_mat_file)

        self.combo_weighting = QComboBox()
        self.combo_weighting.addItems(['Wk', 'Wa', 'Wd'])
        self.combo_weighting.currentIndexChanged.connect(self.evaluate_vibration)

        self.label_rms_x = QLabel("Weighted RMS X: N/A")
        self.label_rms_y = QLabel("Weighted RMS Y: N/A")
        self.label_rms_z = QLabel("Weighted RMS Z: N/A")

        # Plot
        self.plot_canvas = FigureCanvas(Figure(figsize=(8, 5)))
        self.ax = self.plot_canvas.figure.subplots(3, 1, sharex=True)
        self.ax[0].set_title("Acceleration X Axis")
        self.ax[1].set_title("Acceleration Y Axis")
        self.ax[2].set_title("Acceleration Z Axis")

        # Layout
        control_layout.addWidget(self.btn_load)
        control_layout.addWidget(QLabel("Frequency Weighting"))
        control_layout.addWidget(self.combo_weighting)
        control_layout.addStretch()

        main_layout.addLayout(control_layout)
        main_layout.addWidget(self.label_rms_x)
        main_layout.addWidget(self.label_rms_y)
        main_layout.addWidget(self.label_rms_z)
        main_layout.addWidget(self.plot_canvas)

        self.setLayout(main_layout)

    def load_mat_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open .mat File", "", "MAT Files (*.mat)")
        if not filename:
            return

        try:
            mat_data = loadmat(filename)
            print("Loaded .mat keys:", mat_data.keys())

            # Detect first numeric array as X
            numeric_vars = {k: v for k, v in mat_data.items() if isinstance(v, np.ndarray) and v.size > 1}
            if not numeric_vars:
                QMessageBox.warning(self, "Error", "No numeric data found in .mat file.")
                return

            first_var = list(numeric_vars.keys())[0]
            x = numeric_vars[first_var].flatten()
            print(f"Using '{first_var}' as X-axis data, length: {len(x)}")

            # Optional: detect fs if exists
            fs_candidates = ['fs', 'Fs', 'sampling_rate']
            fs = None
            for f in fs_candidates:
                if f in mat_data:
                    fs_var = mat_data[f]
                    fs = float(fs_var) if np.isscalar(fs_var) else float(fs_var.flatten()[0])
                    break

            # Ask user if fs not found
            if fs is None:
                fs, ok = QInputDialog.getDouble(self, "Sampling Frequency", "Enter sampling frequency (Hz):", 1000.0, 0.1, 1e6, 1)
                if not ok:
                    QMessageBox.warning(self, "Error", "Sampling frequency not provided.")
                    return

            # Prepare data dictionary (fill Y/Z with zeros if missing)
            self.data = {
                'x': x,
                'y': np.zeros_like(x),
                'z': np.zeros_like(x)
            }
            self.fs = fs

            # Optional: downsample for huge datasets
            max_points = 50000
            if len(self.data['x']) > max_points:
                factor = len(self.data['x']) // max_points
                print(f"Downsampling by factor {factor} for faster plotting")
                for key in ['x', 'y', 'z']:
                    self.data[key] = self.data[key][::factor]
                self.fs /= factor

            self.evaluate_vibration()

        except Exception as e:
            QMessageBox.critical(self, "Load Error", f"Failed to load .mat file:\n{str(e)}")

    def evaluate_vibration(self):
        if self.data is None or self.fs is None:
            return

        weighting = self.combo_weighting.currentText()
        print("Evaluating with weighting:", weighting)

        x_weighted = apply_frequency_weighting(self.data['x'], self.fs, weighting)
        y_weighted = apply_frequency_weighting(self.data['y'], self.fs, weighting)
        z_weighted = apply_frequency_weighting(self.data['z'], self.fs, weighting)

        rms_x = calculate_weighted_rms(x_weighted)
        rms_y = calculate_weighted_rms(y_weighted)
        rms_z = calculate_weighted_rms(z_weighted)

        self.label_rms_x.setText(f"Weighted RMS X: {rms_x:.4f} m/s²")
        self.label_rms_y.setText(f"Weighted RMS Y: {rms_y:.4f} m/s²")
        self.label_rms_z.setText(f"Weighted RMS Z: {rms_z:.4f} m/s²")

        time = np.arange(len(self.data['x'])) / self.fs

        # Plot X
        self.ax[0].clear()
        self.ax[0].plot(time, self.data['x'], label='Raw X')
        self.ax[0].plot(time, x_weighted, label=f'Weighted X ({weighting})')
        self.ax[0].legend()
        self.ax[0].set_ylabel('Acceleration (m/s²)')

        # Plot Y
        self.ax[1].clear()
        self.ax[1].plot(time, self.data['y'], label='Raw Y')
        self.ax[1].plot(time, y_weighted, label=f'Weighted Y ({weighting})')
        self.ax[1].legend()
        self.ax[1].set_ylabel('Acceleration (m/s²)')

        # Plot Z
        self.ax[2].clear()
        self.ax[2].plot(time, self.data['z'], label='Raw Z')
        self.ax[2].plot(time, z_weighted, label=f'Weighted Z ({weighting})')
        self.ax[2].legend()
        self.ax[2].set_ylabel('Acceleration (m/s²)')
        self.ax[2].set_xlabel('Time (s)')

        self.plot_canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = VibrationEvaluator()
    window.show()
    sys.exit(app.exec_())
