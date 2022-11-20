# Text to use between components
spacer = ' | '

# Disable if not using statuscmd
enable_signal_text = False

# Format string for the date command
date_time_format = '+\"%Y-%m-%d %A %-I:%M %P\"'

# Interval in seconds between updating memory status
memory_interval = 2.

# Enable using nvidia-smi to get GPU memory usage
memory_enable_gpu = False

# Path to a file that indicates that battery conservation mode is active or not
# Use a blank string to disable checking for conservation mode
battery_conservation_mode_path = ''

# The percentage above which the battery is considered fully charged in conservation mode
battery_conservation_mode_full_percent = 55

# Dictionary of audio sink/source name SUFFIXES to abbreviations
volume_source_sink_abbreviations = {
    'analog-stereo': 'A',  # Internal speaker
    'hdmi-stereo': 'H',  # External (HDMI) speaker
}

# Print audio sink/source names with:
#   import pulsectl
#   pulse = pulsectl.Pulse()
#   print([sink.name for sink in pulse.sink_list()])
#   print([source.name for source in pulse.source_list()])

# Abbreviation to use if a sink/source name suffix isn't found
volume_source_sink_unknown_abbreviation = 'U'