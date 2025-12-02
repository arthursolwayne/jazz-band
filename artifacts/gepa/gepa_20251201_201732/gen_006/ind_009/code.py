
import pretty_midi
import numpy as np

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Constants
BPM = 160
BAR_DURATION = 60 / BPM * 4  # 4 bars = 6 seconds
BEAT_DURATION = 60 / BPM  # 0.375 seconds per beat
NOTE_DURATION = 0.25  # quarter note

# Create instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# DRUMS - Bar 1
# Kick on 1 & 3, Snare on 2 & 4, Hihat on every 8th
for beat in range(4):
    time = beat * BEAT_DURATION
    if beat % 2 == 0:  # Kick on 1 & 3
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + NOTE_DURATION))
    if beat % 2 == 1:  # Snare on 2 & 4
        drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + NOTE_DURATION))
    # Hihat every 8th
    for eighth in range(2):
        hihat_time = time + (eighth * BEAT_DURATION / 2)
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.125))

# BASS - Walking line in F minor
# Fm chord: F, Ab, D, F
# Walking line with chromatic approach
bass_notes = [
    # Bar 1
    64,  # F (root)
    62,  # Eb (chromatic approach)
    67,  # Gb (5th)
    64,  # F (root)

    # Bar 2
    69,  # Ab (b3)
    71,  # Bb (chromatic)
    76,  # D (7th)
    73,  # C (chromatic)

    # Bar 3
    69,  # Ab (b3)
    67,  # Gb (5th)
    64,  # F (root)
    62,  # Eb (chromatic)

    # Bar 4
    64,  # F (root)
    67,  # Gb (5th)
    69,  # Ab (b3)
    71,  # Bb (chromatic)
]

# Map to time
for i, note in enumerate(bass_notes):
    time = i * (BEAT_DURATION / 4)  # 16th note spacing
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + NOTE_DURATION / 2))

# PIANO - Open voicings, resolve on last chord
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Dm7 (D, F, Ab, C)
chords = [
    # Bar 2
    [64, 69, 60, 62],  # Fm7
    # Bar 3
    [71, 76, 64, 69],  # Bb7
    # Bar 4
    [67, 64, 69, 60],  # Dm7
]

for i, chord in enumerate(chords):
    time = i * BEAT_DURATION + 0.5  # on beat 2 of each bar
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.5))

# SAX - Concise motif: F -> Ab -> D -> F (with a chromatic run)
sax_notes = [
    # Bar 2
    64,  # F
    66,  # Gb
    69,  # Ab
    71,  # Bb
    # Bar 3
    69,  # Ab
    67,  # Gb
    64,  # F
    # Bar 4
    64,  # F
    69,  # Ab
    67,  # Gb
    64,  # F
]

for i, note in enumerate(sax_notes):
    time = (i // 4) * BEAT_DURATION + (i % 4) * BEAT_DURATION / 4
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + NOTE_DURATION / 2))

# Add instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Save the MIDI file
pm.write("wayne_intro.mid")
print("MIDI file saved as 'wayne_intro.mid'")
