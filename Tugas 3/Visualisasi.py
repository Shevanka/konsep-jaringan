import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import numpy as np

# Parameter sinyal dasar
f0 = 1.0  # Frekuensi fundamental dalam Hz
t = np.linspace(0, 2, 1000)  # Rentang waktu 2 detik
allowed_harmonics = list(range(1, 26, 2))

fig, (ax_time, ax_freq) = plt.subplots(2, 1, figsize=(9, 7))
plt.subplots_adjust(left=0.1, bottom=0.22, hspace=0.4)


def compute_fourier_series(max_h):
  # Gelombang kotak dibentuk oleh harmonisa ganjil: sum((4 / (pi * n)) * sin(2 * pi * n * f0 * t))
  wave = np.zeros_like(t)
  all_n = np.arange(1, 26)
  amplitudes = np.zeros(25)

  for n in range(1, max_h + 1):
    if n % 2 != 0:
      amp = 4 / (np.pi * n)
      wave += amp * np.sin(2 * np.pi * n * f0 * t)
      amplitudes[n - 1] = amp
    else:
      amplitudes[n - 1] = 0.0

  return wave, all_n, amplitudes


# Tampilan awal pada harmonisa n = 1
initial_h = 1
wave, harms, amps = compute_fourier_series(initial_h)

(line_time,) = ax_time.plot(
    t, wave, color='royalblue', lw=2, label='Sinyal Sintesis'
)
ax_time.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax_time.set_ylim(-1.5, 1.5)
ax_time.set_title(f'Domain Waktu: Sintesis Menuju Gelombang Kotak (n = {initial_h})')
ax_time.set_xlabel('Waktu (detik)')
ax_time.set_ylabel('Amplitudo')
ax_time.grid(True, linestyle=':', alpha=0.6)
ax_time.legend(loc='upper right')

bars = ax_freq.bar(harms, amps, color='crimson', width=0.5, edgecolor='black')
ax_freq.set_ylim(0, 1.5)
ax_freq.set_xticks(harms)
ax_freq.set_title('Domain Frekuensi: Spektrum Amplitudo Tiap Harmonisa')
ax_freq.set_xlabel('Harmonisa ke-n')
ax_freq.set_ylabel('Amplitudo')
ax_freq.grid(True, axis='y', linestyle=':', alpha=0.6)

# Penggeser interaktif
slider_ax = plt.axes([0.15, 0.08, 0.7, 0.04])
slider = Slider(
    slider_ax,
    'Harmonisa',
    valmin=1,
    valmax=25,
    valinit=initial_h,
    valstep=allowed_harmonics,
)


def update(val):
  current_h = int(slider.val)
  new_wave, _, new_amps = compute_fourier_series(current_h)

  line_time.set_ydata(new_wave)
  ax_time.set_title(
    f'Domain Waktu: Sintesis Menuju Gelombang Kotak (n = {current_h})'
  )

  for bar, amp in zip(bars, new_amps):
    bar.set_height(amp)

  fig.canvas.draw_idle()


slider.on_changed(update)
plt.show()