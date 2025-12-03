
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F major (no sharps or flats)
key = 'F'

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # Using piano for drum kit (we’ll manually define drum notes)
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')

# Create instruments
bass_instrument = pretty_midi.Instrument(program=bass_program)
piano_instrument = pretty_midi.Instrument(program=piano_program)
drum_instrument = pretty_midi.Instrument(program=drums_program)
sax_instrument = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass_instrument, piano_instrument, drum_instrument, sax_instrument]

# Bar length in seconds at 160 BPM
# 160 BPM = 60 / 160 = 0.375 seconds per beat
# 4/4 time, so one bar = 4 beats = 1.5 seconds

# Bar 1: Little Ray (Drums) only — Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# MIDI note numbers for drum kit (using General MIDI mapping)
# Kick: 36, Snare: 38, Hihat: 42

# Bar 1 (0.0 to 1.5 seconds)
bar1_start = 0.0
bar1_end = 1.5

# Kick on 1 and 3
kick_times = [bar1_start + 0.375, bar1_start + 0.75]  # 1 and 3
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drum_instrument.notes.append(note)

# Snare on 2 and 4
snare_times = [bar1_start + 0.75, bar1_start + 1.125]  # 2 and 4
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drum_instrument.notes.append(note)

# Hihat on every eighth note
hihat_times = [bar1_start + 0.375 * i for i in range(8)]
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drum_instrument.notes.append(note)

# Bar 2: Everyone comes in. Sax takes the melody, piano comps, bass walks.

# Bar 2 starts at 1.5 seconds
bar2_start = 1.5
bar2_end = 3.0

# Bass line: Walking line, roots and fifths with chromatic approaches
# F major scale: F, G, A, Bb, B, C, D
# Root: F (66), 5th: C (60)
# Chromatic approach: E (64) before F, B (62) before C

# Bar 2: F7 (F, A, C, E) -> chromatic approach on F
# So bass line: E (64), F (66), C (60), B (62), G (67), A (69), D (62), C (60)

bass_line = [
    (64, bar2_start + 0.375, bar2_start + 0.75),  # E, beat 1
    (66, bar2_start + 0.75, bar2_start + 1.125),  # F, beat 2
    (60, bar2_start + 1.125, bar2_start + 1.5),   # C, beat 3
    (62, bar2_start + 1.5, bar2_start + 1.875),   # B, beat 4
]

for pitch, start, end in bass_line:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass_instrument.notes.append(note)

# Piano comp: Open voicings, different chord each bar
# Bar 2: F7 (F, A, C, E)
# Open voicing: F (66), A (69), C (60), E (64)
# Comp on beat 2 and 4

piano_notes = [
    # Beat 2: F7
    (66, bar2_start + 0.75, bar2_start + 1.125),
    (69, bar2_start + 0.75, bar2_start + 1.125),
    (60, bar2_start + 0.75, bar2_start + 1.125),
    (64, bar2_start + 0.75, bar2_start + 1.125),

    # Beat 4: G7 (G, B, D, F)
    (67, bar2_start + 1.5, bar2_start + 1.875),
    (71, bar2_start + 1.5, bar2_start + 1.875),
    (62, bar2_start + 1.5, bar2_start + 1.875),
    (66, bar2_start + 1.5, bar2_start + 1.875),
]

for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano_instrument.notes.append(note)

# Sax melody: One short motif, make it sing.
# F -> A -> Bb -> F
# Start on beat 1, end on beat 3.5

sax_notes = [
    (66, bar2_start + 0.375, bar2_start + 0.75),  # F
    (69, bar2_start + 0.75, bar2_start + 1.125),  # A
    (67, bar2_start + 1.125, bar2_start + 1.5),   # Bb
    (66, bar2_start + 1.5, bar2_start + 1.875),   # F
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax_instrument.notes.append(note)

# Bar 3: Everyone plays in sync. Piano comps, bass walks, drums kick in.

bar3_start = 3.0
bar3_end = 4.5

# Bass line: G (G7) -> chromatic approach on G
# G (67), F# (65), A (69), G (67), B (62), C (60), D (62), C (60)

bass_line = [
    (65, bar3_start + 0.375, bar3_start + 0.75),  # F#, beat 1
    (67, bar3_start + 0.75, bar3_start + 1.125),  # G, beat 2
    (69, bar3_start + 1.125, bar3_start + 1.5),   # A, beat 3
    (67, bar3_start + 1.5, bar3_start + 1.875),   # G, beat 4
]

for pitch, start, end in bass_line:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass_instrument.notes.append(note)

# Piano comp: G7 (G, B, D, F)
# Comp on beat 2 and 4

piano_notes = [
    # Beat 2: G7
    (67, bar3_start + 0.75, bar3_start + 1.125),
    (71, bar3_start + 0.75, bar3_start + 1.125),
    (62, bar3_start + 0.75, bar3_start + 1.125),
    (66, bar3_start + 0.75, bar3_start + 1.125),

    # Beat 4: C7 (C, E, G, B)
    (60, bar3_start + 1.5, bar3_start + 1.875),
    (64, bar3_start + 1.5, bar3_start + 1.875),
    (67, bar3_start + 1.5, bar3_start + 1.875),
    (71, bar3_start + 1.5, bar3_start + 1.875),
]

for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano_instrument.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Same pattern as Bar 1, but with a little more energy

# Kick on 1 and 3
kick_times = [bar3_start + 0.375, bar3_start + 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drum_instrument.notes.append(note)

# Snare on 2 and 4
snare_times = [bar3_start + 0.75, bar3_start + 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drum_instrument.notes.append(note)

# Hihat on every eighth note
hihat_times = [bar3_start + 0.375 * i for i in range(8)]
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drum_instrument.notes.append(note)

# Bar 4: Final bar, everyone plays in, sax resolves the motif
bar4_start = 4.5
bar4_end = 6.0

# Bass line: C (C7) -> chromatic approach on C
# B (62), C (60), E (64), C (60), D (62), E (64), F (66), E (64)

bass_line = [
    (62, bar4_start + 0.375, bar4_start + 0.75),  # B, beat 1
    (60, bar4_start + 0.75, bar4_start + 1.125),  # C, beat 2
    (64, bar4_start + 1.125, bar4_start + 1.5),   # E, beat 3
    (60, bar4_start + 1.5, bar4_start + 1.875),   # C, beat 4
]

for pitch, start, end in bass_line:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=end)
    bass_instrument.notes.append(note)

# Piano comp: C7 (C, E, G, B)
# Comp on beat 2 and 4

piano_notes = [
    # Beat 2: C7
    (60, bar4_start + 0.75, bar4_start + 1.125),
    (64, bar4_start + 0.75, bar4_start + 1.125),
    (67, bar4_start + 0.75, bar4_start + 1.125),
    (71, bar4_start + 0.75, bar4_start + 1.125),

    # Beat 4: F7 (F, A, C, E)
    (66, bar4_start + 1.5, bar4_start + 1.875),
    (69, bar4_start + 1.5, bar4_start + 1.875),
    (60, bar4_start + 1.5, bar4_start + 1.875),
    (64, bar4_start + 1.5, bar4_start + 1.875),
]

for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    piano_instrument.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Same pattern as previous bars

# Kick on 1 and 3
kick_times = [bar4_start + 0.375, bar4_start + 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drum_instrument.notes.append(note)

# Snare on 2 and 4
snare_times = [bar4_start + 0.75, bar4_start + 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drum_instrument.notes.append(note)

# Hihat on every eighth note
hihat_times = [bar4_start + 0.375 * i for i in range(8)]
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drum_instrument.notes.append(note)

# Sax motif: Resolves back to F
sax_notes = [
    (69, bar4_start + 0.375, bar4_start + 0.75),  # A, beat 1
    (67, bar4_start + 0.75, bar4_start + 1.125),  # Bb, beat 2
    (66, bar4_start + 1.125, bar4_start + 1.5),   # F, beat 3
    (66, bar4_start + 1.5, bar4_start + 1.875),   # F, beat 4
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax_instrument.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
