
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
               1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Bar 2: Sax enters with motif (1.5 - 3.0s)
# Motif: C (60) -> E (64) -> B (67) -> D (62) -> C (60)
#        1.5s     1.75s    2.0s     2.25s    2.5s

notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.75)
]

sax.notes.extend(notes)

# Marcus (Bass): Walking line in C (60)
# Bar 2: C -> D -> Eb -> F -> G -> A -> Bb -> C
#        1.5s  1.75s  2.0s  2.25s  2.5s  2.75s  3.0s  3.25s

notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=80, pitch=63, start=2.0, end=2.25),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=69, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.5)
]

bass.notes.extend(notes)

# Diane (Piano): 7th chords on 2 and 4 (1.5 - 3.0s)
# Bar 2: C7 on beat 2 (1.75s) and G7 on beat 4 (2.5s)

# C7: C (60), E (64), B (67), D (62)
# G7: G (67), B (69), D (62), F (65)

# C7 on beat 2 (1.75s)
notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0)
]

# G7 on beat 4 (2.5s)
notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75)
])

piano.notes.extend(notes)

# Bar 3: Sax continues motif (3.0 - 4.5s)
# Repeats the motif, but with a slight variation at the end

notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25)
]

sax.notes.extend(notes)

# Marcus (Bass): Walking line in C (60)
# Bar 3: C -> D -> Eb -> F -> G -> A -> Bb -> C
#        3.0s  3.25s  3.5s  3.75s  4.0s  4.25s  4.5s  4.75s

notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=63, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0)
]

bass.notes.extend(notes)

# Diane (Piano): 7th chords on 2 and 4 (3.0 - 4.5s)
# Bar 3: C7 on beat 2 (3.25s) and G7 on beat 4 (4.0s)

# C7 on beat 2 (3.25s)
notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5)
]

# G7 on beat 4 (4.0s)
notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25)
])

piano.notes.extend(notes)

# Bar 4: Sax completes the motif (4.5 - 6.0s)

notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75)
]

sax.notes.extend(notes)

# Marcus (Bass): Walking line in C (60)
# Bar 4: C -> D -> Eb -> F -> G -> A -> Bb -> C
#        4.5s  4.75s  5.0s  5.25s  5.5s  5.75s  6.0s  6.25s

notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.25),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=80, pitch=69, start=5.75, end=6.0),
    pretty_midi.Note(velocity=80, pitch=70, start=6.0, end=6.25),
    pretty_midi.Note(velocity=80, pitch=60, start=6.25, end=6.5)
]

bass.notes.extend(notes)

# Diane (Piano): 7th chords on 2 and 4 (4.5 - 6.0s)
# Bar 4: C7 on beat 2 (4.75s) and G7 on beat 4 (5.5s)

# C7 on beat 2 (4.75s)
notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0)
]

# G7 on beat 4 (5.5s)
notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75)
])

piano.notes.extend(notes)

# Drums: Bar 2 (1.5 - 3.0s)
kick_times = [1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_times = [1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_times = [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
               3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Drums: Bar 3 (3.0 - 4.5s)
kick_times = [3.0, 3.75, 4.5, 5.25]
snare_times = [3.375, 4.125, 4.875, 5.625]
hihat_times = [3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
               4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
kick_times = [4.5, 5.25]
snare_times = [4.875, 5.625]
hihat_times = [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.125)
    drums.notes.append(note)

for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.0625)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
