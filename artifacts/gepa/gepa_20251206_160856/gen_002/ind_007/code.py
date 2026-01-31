
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Set the key to F minor (F, Gb, Ab, Bb, C, Db, Eb)
key = 'Fm'

# Time per bar (160 BPM, 4/4 time)
bpm = 160
time_per_bar = (60 / bpm) * 4  # 6.0 seconds per 4 bars

# Bar duration in seconds
bar_duration = time_per_bar / 4  # 1.5 seconds per bar
beat_duration = bar_duration / 4  # 0.375 seconds per beat

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Drums')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# -------------------
# DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Only hihat and kick on 1
# Bars 2-4: Full rhythm

# Bar 1 (0.0 - 1.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375))  # Hihat on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75)) # Hihat on 2
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125)) # Hihat on 3
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5)) # Hihat on 4

# Bars 2-4 (1.5s - 6.0s)
for bar in range(0, 3):
    start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + (i * 0.375), end=start + (i * 0.375) + 0.125))

# -------------------
# BASS: Marcus
# Walking bass line in Fm, chromatic approach on 2 and 4

# Fm: F, Ab, Bb, C, Eb (for roots)
# Chromatic approach to each chord
# Bar 1: F -> Ab (F -> Gb)
# Bar 2: Ab -> Bb (Ab -> A)
# Bar 3: Bb -> C (Bb -> B)
# Bar 4: C -> Eb (C -> Db)

# Bar durations (start times)
bar_starts = [0.0, 1.5, 3.0, 4.5]

for i, start in enumerate(bar_starts):
    # Root
    root = pretty_midi.Note(velocity=90, pitch=53, start=start, end=start + 0.375)  # F (MIDI 53)
    bass.notes.append(root)

    # Chromatic approach
    chromatic = pretty_midi.Note(velocity=85, pitch=54, start=start + 0.375, end=start + 0.75)  # Gb
    bass.notes.append(chromatic)

    # Next root
    next_root = pretty_midi.Note(velocity=90, pitch=57, start=start + 0.75, end=start + 1.125)  # Ab
    bass.notes.append(next_root)

    # Hit on 3 (Cycle 1-3-5)
    if i == 0:
        bass.notes.append(pretty_midi.Note(velocity=90, pitch=55, start=start + 1.125, end=start + 1.5))  # Bb

# -------------------
# PIANO: Diane
# Open voicings, different chord each bar, resolve on the last

# Bar 1: Fm7 (F, Ab, C, Eb)
# Bar 2: Ab7 (Ab, C, Eb, Gb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: C7 (C, E, G, Bb)

chords = [
    (53, 60, 64, 67),   # Fm7: F, Ab, C, Eb
    (57, 64, 67, 69),   # Ab7: Ab, C, Eb, Gb
    (59, 62, 65, 69),   # Bb7: Bb, D, F, Ab
    (60, 64, 67, 69)    # C7: C, E, G, Bb
]

for i, (note1, note2, note3, note4) in enumerate(chords):
    start = i * 1.5
    # Play each note on the & of 2 and 4
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note1, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note2, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note3, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note4, start=start + 0.375, end=start + 0.75))

# -------------------
# SAX: You
# Short motif, searching, one phrase, leave it hanging

# Bar 1: Start of motif
# Bar 2: Continue
# Bar 3: Continue
# Bar 4: Finish it

# F, Gb, Ab, Bb, C, D, Eb
notes = [53, 54, 57, 59, 60, 62, 64]  # F, Gb, Ab, Bb, C, D, Eb
durations = [0.375, 0.375, 0.375, 0.375, 0.375, 0.375, 0.5]  # last note longer

# Start motif on Bar 1
for i, note in enumerate(notes):
    start = 0.0 + sum(durations[:i])
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + durations[i]))

# Finish on the 4th bar
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.5 + 0.375))  # Bb on Bar 4

# Write to file
pm.write('dante_intro.mid')
print("MIDI file written as 'dante_intro.mid'")
