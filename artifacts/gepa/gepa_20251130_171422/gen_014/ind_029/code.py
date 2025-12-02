
import pretty_midi
from pretty_midi import key_number_to_name

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()

# Set tempo to 160 BPM
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempos = [pretty_midi.TempoChangeEvent(160.0, 0.0)]

# Key: F minor
key = 'F minor'
key_number = pretty_midi.key_name_to_number(key)

# Instrument: Tenor Sax (program 65)
instruments = []

# --- Tenor Saxophone ---
tenor_program = 65
tenor = pretty_midi.Instrument(program=tenor_program)
instruments.append(tenor)

# --- Bass ---
bass_program = 33
bass = pretty_midi.Instrument(program=bass_program)
instruments.append(bass)

# --- Piano ---
piano_program = 0
piano = pretty_midi.Instrument(program=piano_program)
instruments.append(piano)

# --- Drums ---
drums_program = 10
drums = pretty_midi.Instrument(program=drums_program)
instruments.append(drums)

pm.instruments = instruments

# Time constants: 160 BPM = 160 beats per minute
# Each beat = 0.375 seconds (60 / 160 = 0.375)
# Each bar = 4 beats = 1.5 seconds
# Total duration: 4 bars = 6.0 seconds

# --- Bar 1: Drums only ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0

# Kick on beat 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start, end=bar1_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar1_start + 0.75, end=bar1_start + 1.125))

# Snare on beat 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.5))

# Hi-hat on every eighth
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar1_start + i * 0.375, end=bar1_start + i * 0.375 + 0.125))

# --- Bars 2-4: Full Ensemble ---
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Tenor Sax Motif (Fm7 -> Bb7)
# Fm7: F, Ab, C, Eb
# Bb7: Bb, D, F, Ab

# Tenor motif: F, Ab, C, Eb -> Bb, D, F, Ab
# Motif is 4 notes over 4 beats (1 bar), then a repeat with variation (Bar 3), then resolution (Bar 4)

# Bar 2: Tenor Motif (start of motif)
tenor_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=bar2_start, end=bar2_start + 0.375),  # F (tenor sax is transposed)
    pretty_midi.Note(velocity=110, pitch=67, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=bar2_start + 0.75, end=bar2_start + 1.125),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=bar2_start + 1.125, end=bar2_start + 1.5),  # Eb
]

tenor.notes.extend(tenor_notes)

# Bar 3: Motif variation (same rhythm, different notes)
tenor_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=bar3_start, end=bar3_start + 0.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=77, start=bar3_start + 0.375, end=bar3_start + 0.75),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=bar3_start + 1.125, end=bar3_start + 1.5),  # Ab
]

tenor.notes.extend(tenor_notes)

# Bar 4: Motif resolution or return
tenor_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=bar4_start + 0.375, end=bar4_start + 0.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=bar4_start + 0.75, end=bar4_start + 1.125),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=bar4_start + 1.125, end=bar4_start + 1.5),  # Eb
]

tenor.notes.extend(tenor_notes)

# Bass (Marcus): Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=bar2_start + 0.375, end=bar2_start + 0.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=bar2_start + 0.75, end=bar2_start + 1.125),  # F#
    pretty_midi.Note(velocity=90, pitch=52, start=bar2_start + 1.125, end=bar2_start + 1.5),  # G

    pretty_midi.Note(velocity=90, pitch=53, start=bar3_start, end=bar3_start + 0.375),  # G#
    pretty_midi.Note(velocity=90, pitch=54, start=bar3_start + 0.375, end=bar3_start + 0.75),  # A
    pretty_midi.Note(velocity=90, pitch=51, start=bar3_start + 0.75, end=bar3_start + 1.125),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=bar3_start + 1.125, end=bar3_start + 1.5),  # F

    pretty_midi.Note(velocity=90, pitch=49, start=bar4_start, end=bar4_start + 0.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=bar4_start + 0.375, end=bar4_start + 0.75),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=bar4_start + 0.75, end=bar4_start + 1.125),  # F#
    pretty_midi.Note(velocity=90, pitch=52, start=bar4_start + 1.125, end=bar4_start + 1.5),  # G
]

bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comping on 2 and 4
# Fm7 on beat 1 (F, Ab, C, Eb), Bb7 on beat 3 (Bb, D, F, Ab)

# Bar 2: Fm7 on beat 1
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=bar2_start, end=bar2_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=bar2_start, end=bar2_start + 0.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=67, start=bar2_start, end=bar2_start + 0.375),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + 0.375),  # Eb
]

# Bar 2: Bb7 on beat 3
piano_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=74, start=bar2_start + 0.75, end=bar2_start + 1.125))  # D
piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar2_start + 0.75, end=bar2_start + 1.125))  # F
piano_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar2_start + 0.75, end=bar2_start + 1.125))  # Bb

piano.notes.extend(piano_notes)

# Bar 3: Bb7 on beat 1
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start, end=bar3_start + 0.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=bar3_start, end=bar3_start + 0.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=bar3_start, end=bar3_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=71, start=bar3_start, end=bar3_start + 0.375),  # Bb
]

# Bar 3: Fm7 on beat 3
piano_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=bar3_start + 0.75, end=bar3_start + 1.125))  # F
piano_notes.append(pretty_midi.Note(velocity=80, pitch=60, start=bar3_start + 0.75, end=bar3_start + 1.125))  # Ab
piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar3_start + 0.75, end=bar3_start + 1.125))  # C
piano_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=bar3_start + 0.75, end=bar3_start + 1.125))  # Eb

piano.notes.extend(piano_notes)

# Bar 4: Fm7 on beat 1
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=bar4_start, end=bar4_start + 0.375),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=bar4_start, end=bar4_start + 0.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=67, start=bar4_start, end=bar4_start + 0.375),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=bar4_start, end=bar4_start + 0.375),  # Eb
]

# Bar 4: Bb7 on beat 3
piano_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 0.75, end=bar4_start + 1.125))  # Bb
piano_notes.append(pretty_midi.Note(velocity=80, pitch=74, start=bar4_start + 0.75, end=bar4_start + 1.125))  # D
piano_notes.append(pretty_midi.Note(velocity=80, pitch=67, start=bar4_start + 0.75, end=bar4_start + 1.125))  # F
piano_notes.append(pretty_midi.Note(velocity=80, pitch=71, start=bar4_start + 0.75, end=bar4_start + 1.125))  # Bb

piano.notes.extend(piano_notes)

# Drums for Bars 2–4
# Similar to Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat every eighth

# Bar 2
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar2_start + i * 0.375, end=bar2_start + i * 0.375 + 0.125))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + 0.75, end=bar2_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 0.375, end=bar2_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + 1.125, end=bar2_start + 1.5))

# Bar 3
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar3_start + i * 0.375, end=bar3_start + i * 0.375 + 0.125))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + 0.75, end=bar3_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 0.375, end=bar3_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + 1.125, end=bar3_start + 1.5))

# Bar 4
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar4_start + i * 0.375, end=bar4_start + i * 0.375 + 0.125))

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + 0.75, end=bar4_start + 1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 0.375, end=bar4_start + 0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + 1.125, end=bar4_start + 1.5))

# Write MIDI file
pm.write('dante_intro.mid')
print("MIDI file 'dante_intro.mid' created successfully.")
