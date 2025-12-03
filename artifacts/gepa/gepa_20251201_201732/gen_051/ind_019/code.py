
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)

# Bass: Walking line in F minor (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),  # Ab2
    pretty_midi.Note(velocity=80, pitch=75, start=2.625, end=3.0),   # A2
]

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=84, start=1.5, end=1.875),  # E
]

# Sax: Motif - F, G#, A, Bb (one short motif, make it sing)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=110, pitch=79, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=77, start=1.875, end=2.0),   # Bb
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)

# Bass: Walking line in F minor (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),  # B2
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.125),  # C2
    pretty_midi.Note(velocity=80, pitch=78, start=4.125, end=4.5),   # Db2
]

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # F
]

# Sax: Motif - G#, A, Bb, C (continuation of motif)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=78, start=3.0, end=3.125),  # G#
    pretty_midi.Note(velocity=110, pitch=79, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=77, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=80, start=3.375, end=3.5),   # C
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full ensemble (4.5 - 6.0s)

# Bass: Walking line in F minor (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),  # G2
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),  # Ab2
    pretty_midi.Note(velocity=80, pitch=75, start=5.625, end=6.0),   # A2
]

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=84, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # Bb
]

# Sax: Motif - F, G#, A, Bb (return to the motif, finish it)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=4.625, end=4.75),  # G#
    pretty_midi.Note(velocity=110, pitch=79, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=110, pitch=77, start=4.875, end=5.0),   # Bb
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
