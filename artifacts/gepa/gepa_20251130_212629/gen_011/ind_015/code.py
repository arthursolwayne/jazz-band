
import mido
from mido import Message, MidiFile, MidiTrack
import time

# Setup
mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

# Tempo
track.append(mido.MetaMessage('set_tempo', tempo=mido.bpm2tempo(160)))

# Key: D Major
# D = 62, G = 67, A = 69, B = 71, etc.

# Instrument: Tenor Sax (program 64)
track.append(Message('program_change', program=64, channel=0))

# Channel assignments
# Tenor Sax: Channel 0
# Bass: Channel 1
# Piano: Channel 2
# Drums: Channel 9

# Define time (in ticks) per beat: 480 ticks/beat is standard
# 160 BPM = 1 beat = 0.75 seconds
# 480 ticks/beat => 1 tick = 0.75 / 480 = 0.0015625 seconds

# Define 4 bars (6 seconds) at 160 BPM
# Each bar = 4 beats => 4 * 480 = 1920 ticks
# 4 bars = 7680 ticks

# Define note duration in ticks
def note_duration(beats):
    return int(beats * 480)

# Bar 1: Drums only — 4/4 time, kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def bar1():
    # Kick on 1 and 3
    track.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
    track.append(Message('note_off', note=36, velocity=100, time=note_duration(1), channel=9))
    track.append(Message('note_on', note=36, velocity=100, time=note_duration(2), channel=9))
    track.append(Message('note_off', note=36, velocity=100, time=note_duration(1), channel=9))

    # Snare on 2 and 4
    track.append(Message('note_on', note=38, velocity=110, time=note_duration(1), channel=9))
    track.append(Message('note_off', note=38, velocity=110, time=note_duration(1), channel=9))
    track.append(Message('note_on', note=38, velocity=110, time=note_duration(2), channel=9))
    track.append(Message('note_off', note=38, velocity=110, time=note_duration(1), channel=9))

    # Hi-hat on every eighth
    for i in range(8):
        track.append(Message('note_on', note=42, velocity=80, time=note_duration(0.5), channel=9))
        track.append(Message('note_off', note=42, velocity=80, time=note_duration(0.5), channel=9))

# Bar 2-3: Everyone in, tenor sax takes the melody
def bar2():
    # Bass: Walking line, chromatic approach to D
    track.append(Message('note_on', note=62, velocity=90, time=0, channel=1))
    track.append(Message('note_off', note=62, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=63, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=63, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=64, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=64, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=65, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=65, velocity=90, time=note_duration(0.5), channel=1))

    # Piano: 7th chords on 2 and 4
    track.append(Message('note_on', note=67, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_on', note=71, velocity=80, time=0, channel=2))
    track.append(Message('note_on', note=74, velocity=80, time=0, channel=2))
    track.append(Message('note_on', note=76, velocity=80, time=0, channel=2))
    track.append(Message('note_off', note=67, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=71, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=74, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=76, velocity=80, time=note_duration(1), channel=2))

    # Tenor Sax: Motif — D (62), F# (66), A (69), rest
    track.append(Message('note_on', note=62, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=62, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=69, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=69, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=62, velocity=110, time=note_duration(0.5), channel=0))  # Repeat D
    track.append(Message('note_off', note=62, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=69, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=69, velocity=110, time=note_duration(0.5), channel=0))

    # Drums: Continue with kick, snare, hihat
    track.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
    track.append(Message('note_off', note=36, velocity=100, time=note_duration(1), channel=9))
    track.append(Message('note_on', note=38, velocity=110, time=note_duration(1), channel=9))
    track.append(Message('note_off', note=38, velocity=110, time=note_duration(1), channel=9))
    for i in range(4):
        track.append(Message('note_on', note=42, velocity=80, time=note_duration(0.5), channel=9))
        track.append(Message('note_off', note=42, velocity=80, time=note_duration(0.5), channel=9))

def bar3():
    # Bass: Walking line, chromatic approach to G
    track.append(Message('note_on', note=67, velocity=90, time=0, channel=1))
    track.append(Message('note_off', note=67, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=68, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=68, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=69, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=69, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=70, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=70, velocity=90, time=note_duration(0.5), channel=1))

    # Piano: 7th chords on 2 and 4
    track.append(Message('note_on', note=67, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_on', note=71, velocity=80, time=0, channel=2))
    track.append(Message('note_on', note=74, velocity=80, time=0, channel=2))
    track.append(Message('note_on', note=76, velocity=80, time=0, channel=2))
    track.append(Message('note_off', note=67, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=71, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=74, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=76, velocity=80, time=note_duration(1), channel=2))

    # Tenor Sax: Continue motif — D (62), F# (66), A (69), rest
    track.append(Message('note_on', note=62, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=62, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=69, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=69, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=62, velocity=110, time=note_duration(0.5), channel=0))  # Repeat D
    track.append(Message('note_off', note=62, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=66, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=69, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=69, velocity=110, time=note_duration(0.5), channel=0))

    # Drums: Continue with kick, snare, hihat
    track.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
    track.append(Message('note_off', note=36, velocity=100, time=note_duration(1), channel=9))
    track.append(Message('note_on', note=38, velocity=110, time=note_duration(1), channel=9))
    track.append(Message('note_off', note=38, velocity=110, time=note_duration(1), channel=9))
    for i in range(4):
        track.append(Message('note_on', note=42, velocity=80, time=note_duration(0.5), channel=9))
        track.append(Message('note_off', note=42, velocity=80, time=note_duration(0.5), channel=9))

# Bar 4: Tenor Sax ends on a question — E (64), leave it hanging
def bar4():
    # Bass: Chromatic approach to B
    track.append(Message('note_on', note=71, velocity=90, time=0, channel=1))
    track.append(Message('note_off', note=71, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=72, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=72, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=73, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=73, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_on', note=74, velocity=90, time=note_duration(0.5), channel=1))
    track.append(Message('note_off', note=74, velocity=90, time=note_duration(0.5), channel=1))

    # Piano: 7th chords on 2 and 4
    track.append(Message('note_on', note=67, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_on', note=71, velocity=80, time=0, channel=2))
    track.append(Message('note_on', note=74, velocity=80, time=0, channel=2))
    track.append(Message('note_on', note=76, velocity=80, time=0, channel=2))
    track.append(Message('note_off', note=67, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=71, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=74, velocity=80, time=note_duration(1), channel=2))
    track.append(Message('note_off', note=76, velocity=80, time=note_duration(1), channel=2))

    # Tenor Sax: End on E (64), leave it hanging
    track.append(Message('note_on', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_on', note=64, velocity=110, time=note_duration(0.5), channel=0))
    track.append(Message('note_off', note=64, velocity=110, time=note_duration(0.5), channel=0))

    # Drums: Continue with kick, snare, hihat
    track.append(Message('note_on', note=36, velocity=100, time=0, channel=9))
    track.append(Message('note_off', note=36, velocity=100, time=note_duration(1), channel=9))
    track.append(Message('note_on', note=38, velocity=110, time=note_duration(1), channel=9))
    track.append(Message('note_off', note=38, velocity=110, time=note_duration(1), channel=9))
    for i in range(4):
        track.append(Message('note_on', note=42, velocity=80, time=note_duration(0.5), channel=9))
        track.append(Message('note_off', note=42, velocity=80, time=note_duration(0.5), channel=9))

# Generate the intro
bar1()
bar2()
bar3()
bar4()

# Save the MIDI file
mid.save('jazz_intro.mid')
print("Intro saved as 'jazz_intro.mid'")
