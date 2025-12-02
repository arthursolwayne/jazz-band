
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # G

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),   # B

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # F7 - B
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # F7 - D

    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # F7 - B
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # F7 - D

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # F7 - B
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # F7 - D

    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # F7 - B
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # F7 - D

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # F7 - B
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # F7 - D

    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625),  # F7 - B
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # F7 - D
]
for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: short motif, sing, leave it hanging
sax_notes = [
    # Bar 2: start the motif
    pretty_midi.Note(velocity=110, pitch=63, start=1.5, end=1.75),  # G (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # A (F7)

    # Bar 3: leave it hanging
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.25),  # G (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # A (F7)

    # Bar 4: come back and finish it
    pretty_midi.Note(velocity=110, pitch=63, start=4.5, end=4.75),  # G (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # A (F7)
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # F# (F7)
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.5),  # G (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),  # A (F7)
    pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0),  # B (F7)
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
