
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: F minor
key = 'Fm'

# Time per bar (160 BPM => 60 / 160 = 0.375 seconds per beat)
time_per_beat = 0.375
time_per_bar = time_per_beat * 4

# Define instrument programs
tenor_sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

# Create instruments
tenor_sax = pretty_midi.Instrument(program=tenor_sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [tenor_sax, bass, piano, drums]

# Time variable to track position in the piece
time = 0.0

# -------------------------------------
# Bar 1: Drums only - build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time per beat = 0.375s, 8th note = 0.1875s
# Bar 1: 0.0 to 1.5s

# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=0.9375))

# Snare on 2 and 4 (beat 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=41, start=0.375, end=0.5625))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=41, start=1.125, end=1.3125))

# Hihat on every eighth
hihat_pitches = [42, 42, 42, 42, 42, 42, 42, 42]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]
for pitch, start in zip(hihat_pitches, hihat_times):
    drums.notes.append(pretty_midi.Note(velocity=75, pitch=pitch, start=start, end=start + 0.1875))

time += time_per_bar

# -------------------------------------
# Bar 2: Everyone comes in, Tenor sax melody begins
# Fm7 -> Bb7 -> Eb7 -> Ab7 (no modulation)

# Tenor Sax Melody (Fm7 - Bb7 - Eb7 - Ab7)
# Motif: F (D2) -> G# (E2) -> E (D2) -> D (C2)
# Start on beat 1, end on beat 2.625 (end of bar)

# F (F2) starts on beat 1 (0.0), ends on beat 1.125
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=0.0, end=0.1875*6.0))

# G# (E2) starts on beat 1.5 (0.75), ends on beat 1.875
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=73, start=0.75, end=0.9375*6.0))

# E (D2) starts on beat 2.0 (1.125), ends on beat 2.375
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.125, end=1.3125*6.0))

# D (C2) starts on beat 2.5 (1.5), ends on beat 2.75
tenor_sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875*6.0))

# Bass: Fm7 - Bb7 - Eb7 - Ab7
# Roots: F (1), Bb (1), Eb (1), Ab (1)
# Walking bass line: F - Gb - Bb - B (Fm7), Bb - C - Eb - E (Bb7), etc.

# Bar 2 (0.0 to 1.5s)
# Fm7: F, Ab, D, Bb
# Bass line: F -> Gb -> Bb -> A
bass.notes.append(pretty_midi.Note(velocity=70, pitch=71, start=0.0, end=0.375))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=69, start=0.375, end=0.75))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=71, start=0.75, end=1.125))
bass.notes.append(pretty_midi.Note(velocity=70, pitch=69, start=1.125, end=1.5))

# Piano: Open voicings, each bar a different chord, resolve on last beat

# Bar 2: Fm7 (F, Ab, D, Bb)
# Open voicing: F (71), Ab (68), D (62), Bb (70)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=0.0, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=0.0, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=0.0, end=0.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=0.0, end=0.75))

# Bar 3: Bb7 (Bb, D, F, A)
# Open voicing: Bb (70), D (62), F (71), A (69)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.25))

# Bar 4: Eb7 (Eb, G, Bb, D)
# Open voicing: Eb (60), G (67), Bb (70), D (62)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75))

# Bar 4: Drums again, like bar 1
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4: 3.0 to 4.5s

# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375))

# Snare on 2 and 4 (beat 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=110, pitch=41, start=3.375, end=3.5625))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=41, start=4.125, end=4.3125))

# Hihat on every eighth
hihat_times = [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125]
for start in hihat_times:
    drums.notes.append(pretty_midi.Note(velocity=75, pitch=42, start=start, end=start + 0.1875))

# Save the MIDI file
pm.write('wayne_intro.mid')
