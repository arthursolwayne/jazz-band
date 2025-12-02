
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Set tempo to 160 BPM
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Time per beat in seconds (60 seconds / 160 beats per minute)
beat_seconds = 60.0 / 160.0

# Time per bar in seconds (4 beats per bar)
bar_seconds = 4 * beat_seconds  # 1.5 seconds per bar

# Instrument for each player
# Tenor Sax (program 64)
sax_program = 64
sax_instrument = pretty_midi.Instrument(program=sax_program)
pm.instruments.append(sax_instrument)

# Bass (program 33)
bass_program = 33
bass_instrument = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass_instrument)

# Piano (program 0)
piano_program = 0
piano_instrument = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano_instrument)

# Drums (program 128)
drum_program = 128
drum_instrument = pretty_midi.Instrument(program=drum_program)
pm.instruments.append(drum_instrument)

# MIDICode: Define note numbers for Dm7
# Dm7: D, F, A, C
D = 62
F = 64
A = 69
C = 60
Dm7 = [D, F, A, C]

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3
# Snare on 2 and 4
# Hi-hat on every 8th
# Add variation in dynamics

# Time for each 8th note
eighth_note = beat_seconds / 2

# Bar 1 (0 to 1.5 seconds)
time = 0.0
drum_instrument.notes.extend([
    pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + eighth_note),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=49, start=time + eighth_note, end=time + 2 * eighth_note),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=time + 2 * eighth_note, end=time + 3 * eighth_note),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=49, start=time + 3 * eighth_note, end=time + 4 * eighth_note),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=36, start=time + 4 * eighth_note, end=time + 5 * eighth_note),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=49, start=time + 5 * eighth_note, end=time + 6 * eighth_note),  # Hi-hat
    pretty_midi.Note(velocity=80, pitch=42, start=time + 6 * eighth_note, end=time + 7 * eighth_note),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=49, start=time + 7 * eighth_note, end=time + 8 * eighth_note),  # Hi-hat
])

# Bar 2: All instruments enter

# Time for bar 2: 1.5 to 3.0 seconds
time = 1.5

# Bass line (Marcus)
# Walking line in Dm, chromatic approach to D
# Dm: D, F, A, C
# Bass line: F, D, A, C, G, Bb, A, F, E, D, C, B, D, F
# Let's simplify to a 4-bar line that moves from F to D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=time, end=time + beat_seconds),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=time + beat_seconds, end=time + 2 * beat_seconds),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=time + 2 * beat_seconds, end=time + 3 * beat_seconds),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=time + 3 * beat_seconds, end=time + 4 * beat_seconds),  # C
]
bass_instrument.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
# Dm7 on 2 and 4
piano_notes = []
for i in range(2):
    offset = (i + 1) * beat_seconds  # 2 and 4
    for note in Dm7:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note + 12, start=offset, end=offset + beat_seconds / 2))
piano_instrument.notes.extend(piano_notes)

# Tenor Sax (Dante) - Motif: D -> F -> C -> Bb -> D
# Start with D, then resolve with a chromatic run down to Bb, then back to D
# 1st note: D (62), 2nd: F (64), 3rd: C (60), 4th: Bb (58)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=time, end=time + beat_seconds / 2),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=time + beat_seconds / 2, end=time + beat_seconds),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=time + beat_seconds, end=time + 1.5 * beat_seconds),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=time + 1.5 * beat_seconds, end=time + 2 * beat_seconds),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=time + 2 * beat_seconds, end=time + 2.5 * beat_seconds),  # D
]
sax_instrument.notes.extend(sax_notes)

# Bar 3: Continue with group playing
# Time for bar 3: 3.0 to 4.5 seconds

# Drums
# Same pattern as bar 1
for note in drum_instrument.notes:
    note.start += bar_seconds
    note.end += bar_seconds

# Bass line (Marcus) continues
# Chromatic approach to A and C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=time + bar_seconds, end=time + bar_seconds + beat_seconds),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=time + bar_seconds + beat_seconds, end=time + bar_seconds + 2 * beat_seconds),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=time + bar_seconds + 2 * beat_seconds, end=time + bar_seconds + 3 * beat_seconds),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=time + bar_seconds + 3 * beat_seconds, end=time + bar_seconds + 4 * beat_seconds),  # C
]
bass_instrument.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
# Dm7 again
piano_notes = []
for i in range(2):
    offset = (i + 1) * beat_seconds + bar_seconds  # 2 and 4
    for note in Dm7:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note + 12, start=offset, end=offset + beat_seconds / 2))
piano_instrument.notes.extend(piano_notes)

# Tenor Sax - repeat motif with slight variation
# D -> F -> C -> Bb -> D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=time + bar_seconds, end=time + bar_seconds + beat_seconds / 2),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=time + bar_seconds + beat_seconds / 2, end=time + bar_seconds + beat_seconds),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=time + bar_seconds + beat_seconds, end=time + bar_seconds + 1.5 * beat_seconds),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=time + bar_seconds + 1.5 * beat_seconds, end=time + bar_seconds + 2 * beat_seconds),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=time + bar_seconds + 2 * beat_seconds, end=time + bar_seconds + 2.5 * beat_seconds),  # D
]
sax_instrument.notes.extend(sax_notes)

# Bar 4: Continue with group playing
# Time for bar 4: 4.5 to 6.0 seconds

# Drums
for note in drum_instrument.notes:
    note.start += bar_seconds * 2
    note.end += bar_seconds * 2

# Bass line (Marcus) continues
# Chromatic approach to D with a resolution
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=time + 2 * bar_seconds, end=time + 2 * bar_seconds + beat_seconds),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=time + 2 * bar_seconds + beat_seconds, end=time + 2 * bar_seconds + 2 * beat_seconds),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=time + 2 * bar_seconds + 2 * beat_seconds, end=time + 2 * bar_seconds + 3 * beat_seconds),  # G
    pretty_midi.Note(velocity=80, pitch=62, start=time + 2 * bar_seconds + 3 * beat_seconds, end=time + 2 * bar_seconds + 4 * beat_seconds),  # D
]
bass_instrument.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
# Dm7 again
piano_notes = []
for i in range(2):
    offset = (i + 1) * beat_seconds + 2 * bar_seconds  # 2 and 4
    for note in Dm7:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=note + 12, start=offset, end=offset + beat_seconds / 2))
piano_instrument.notes.extend(piano_notes)

# Tenor Sax - repeat motif with slight variation
# D -> F -> C -> Bb -> D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=time + 2 * bar_seconds, end=time + 2 * bar_seconds + beat_seconds / 2),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=time + 2 * bar_seconds + beat_seconds / 2, end=time + 2 * bar_seconds + beat_seconds),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=time + 2 * bar_seconds + beat_seconds, end=time + 2 * bar_seconds + 1.5 * beat_seconds),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=time + 2 * bar_seconds + 1.5 * beat_seconds, end=time + 2 * bar_seconds + 2 * beat_seconds),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=time + 2 * bar_seconds + 2 * beat_seconds, end=time + 2 * bar_seconds + 2.5 * beat_seconds),  # D
]
sax_instrument.notes.extend(sax_notes)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file written as 'dante_russo_intro.mid'")
