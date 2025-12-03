
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1, 3; snare on 2, 4; hihat every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Start of the quartet
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),  # F (D2)
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # Ab (D#2)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G (D2)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # Ab (D#2)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=2.25),  # E

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=3.0),  # Ab

    # Bar 4: E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.75),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, haunting but incomplete
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=73, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=74, start=2.625, end=3.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0)
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
