
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Set key to F minor
key = 'Fm'

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Using piano for drums (placeholder)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instrument tracks
drum_instrument = pretty_midi.Instrument(program=drums_program)
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drum_instrument, bass_instrument, piano_instrument, sax_instrument]

# BPM = 160, 4/4 time
# 1 beat = 0.375 seconds, 1 bar = 1.5 seconds
# 4 bars = 6 seconds

# Bar 1: Drums only - sparse, tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use piano instrument to represent drum hits for simplicity

# Bar 1
bar_duration = 1.5
start_time = 0.0

# Kick on 1 and 3
kick_times = [0.0, 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t + start_time, end=t + start_time + 0.1)
    drum_instrument.notes.append(note)

# Snare on 2 and 4
snare_times = [0.375, 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t + start_time, end=t + start_time + 0.1)
    drum_instrument.notes.append(note)

# Hi-hat on every eighth note
for i in range(8):
    t = i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=42, start=t + start_time, end=t + start_time + 0.05)
    drum_instrument.notes.append(note)

# Bar 2: Everyone enters, bass line, piano chords, sax melody

# Bass line: Fm - chromatic approach to Bb
# Fm: F, Ab, Db, Eb
# Chromatic approach to Bb: Ab, G, G#, Bb
# Start from Ab and move down to Bb

# Bass line in bars 2-4
bass_notes = [
    # Bar 2 (measure 2)
    (0.0, 64),  # Ab
    (0.375, 67),  # G
    (0.75, 69),  # G#
    (1.125, 71),  # Bb
    # Bar 3 (measure 3)
    (1.5, 71),  # Bb
    (1.875, 74),  # C
    (2.25, 76),  # D
    (2.625, 64),  # Ab
    # Bar 4 (measure 4)
    (3.0, 64),  # Ab
    (3.375, 67),  # G
    (3.75, 69),  # G#
    (4.125, 71),  # Bb
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.25)
    bass_instrument.notes.append(note)

# Piano: 7th chords, comp on 2 and 4

# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Cm7 = C, Eb, G, Bb
# Dm7 = D, F, A, C
# We'll use Fm7 on 2 and 4

# Bar 2
chord_start = 1.5
chord_duration = 0.375
chord_notes = [53, 56, 58, 60]  # F, Ab, Bb, C (Fm7)

for pitch in chord_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=chord_start, end=chord_start + chord_duration)
    piano_instrument.notes.append(note)

# Bar 4
chord_start = 3.0
chord_duration = 0.375
chord_notes = [53, 56, 58, 60]  # F, Ab, Bb, C (Fm7)

for pitch in chord_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=chord_start, end=chord_start + chord_duration)
    piano_instrument.notes.append(note)

# Sax melody: One short motif, space, tension, resolution

# Motif: F, Bb, Eb, G
# Notes: F (53), Bb (58), Eb (56), G (58 or 60? Let's use 60 for G)
# Start on beat 1 of bar 2 (1.5s), play first 3 notes, leave last on beat 3 of bar 2 (2.25s), then resolve in bar 4

melody_notes = [
    (1.5, 53, 0.5),  # F
    (2.0, 58, 0.5),  # Bb
    (2.5, 56, 0.5),  # Eb
    (3.0, 60, 1.0),  # G (hold to end of bar 4)
]

for start, pitch, duration in melody_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + duration)
    sax_instrument.notes.append(note)

# Save the MIDI file
pm.write('dante_intro.mid')
