
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=3.0), # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875), # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875), # C
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375), # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375), # F
    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875), # B
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (D, F#, B)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75), # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875), # B
    # Bar 3: Leave it hanging (nothing until bar 4)
    # Bar 4: Come back and finish it (D, G, A)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75), # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=4.875), # A
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Drums (4.5 - 6.0s)
# Same pattern as bar 1
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

# Add remaining drum notes for bar 4
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]
drums.notes.extend(drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_moment.mid")
