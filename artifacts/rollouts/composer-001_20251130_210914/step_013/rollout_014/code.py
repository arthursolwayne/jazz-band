
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D7 -> F#7 -> B7 -> D7
# Motif: D (start), F# (leave hanging), B (come back), D (resolve)

sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5))  # F#
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.875, end=3.125))  # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))  # D

# BASS: Walking line, chromatic approaches, never the same note twice
# D -> Eb -> F -> G -> A -> Bb -> B -> C -> D

bass_notes = [
    (62, 1.5, 1.625),  # D
    (63, 1.625, 1.75), # Eb
    (64, 1.75, 1.875), # F
    (65, 1.875, 2.0),  # G
    (67, 2.0, 2.125),  # A
    (68, 2.125, 2.25), # Bb
    (69, 2.25, 2.375), # B
    (71, 2.375, 2.5),  # C
    (62, 2.5, 2.625),  # D
    (63, 2.625, 2.75), # Eb
    (64, 2.75, 2.875), # F
    (65, 2.875, 3.0),  # G
    (67, 3.0, 3.125),  # A
    (68, 3.125, 3.25), # Bb
    (69, 3.25, 3.375), # B
    (71, 3.375, 3.5),  # C
    (62, 3.5, 3.625),  # D
    (63, 3.625, 3.75), # Eb
    (64, 3.75, 3.875), # F
    (65, 3.875, 4.0),  # G
    (67, 4.0, 4.125),  # A
    (68, 4.125, 4.25), # Bb
    (69, 4.25, 4.375), # B
    (71, 4.375, 4.5),  # C
    (62, 4.5, 4.625),  # D
    (63, 4.625, 4.75), # Eb
    (64, 4.75, 4.875), # F
    (65, 4.875, 5.0),  # G
]

for pitch, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end))

# PIANO: 7th chords, comp on 2 and 4

# Bar 2 (1.5 - 2.0s): D7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=2.0))  # D
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=2.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=2.0))  # A
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=2.0))  # C#

# Bar 3 (2.5 - 3.0s): F#7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=3.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=3.0))  # A#
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=2.5, end=3.0))  # C#
piano.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=2.5, end=3.0))  # E

# Bar 4 (3.5 - 4.0s): B7
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=4.0))  # B
piano.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=3.5, end=4.0))  # D#
piano.notes.append(pretty_midi.Note(velocity=80, pitch=80, start=3.5, end=4.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=80, pitch=84, start=3.5, end=4.0))  # G#

# Drums in bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3 of each bar
for i in range(1, 4):
    start = 1.5 + i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))

# Snare on 2 and 4 of each bar
for i in range(1, 4):
    start = 1.5 + i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))

# Hi-hat on every eighth
for i in range(1, 4):
    start = 1.5 + i * 1.5
    for j in range(0, 4):
        hihat_start = start + j * 0.375
        hihat_end = hihat_start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("wayne_intro.mid")
