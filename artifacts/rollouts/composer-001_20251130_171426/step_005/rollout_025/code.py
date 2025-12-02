
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
    # Hihat on every eighth
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

# Bars 2-4 (1.5 - 6.0s)
# Bass line (Marcus) - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # G#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=47, start=4.125, end=4.5),  # C
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.875 - 2.25s) - F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.875, end=2.25),  # E
    # Bar 2, beat 4 (2.625 - 3.0s) - F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0),  # E
    # Bar 3, beat 2 (3.375 - 3.75s) - F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75),  # E
    # Bar 3, beat 4 (4.125 - 4.5s) - F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5),  # E
    # Bar 4, beat 2 (4.875 - 5.25s) - F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=4.875, end=5.25),  # E
    # Bar 4, beat 4 (5.625 - 6.0s) - F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - 4 bars, one short motif, make it sing
# Start on F (65), move to A (69), then G (67), then F (65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # F
    # Repeat the motif, start again at 3.0s
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # F
    # Repeat the motif again at 4.5s
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # F
    # End on a suspended note, leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continuation of bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
]
# Snare on 2 and 4
drum_notes_bar2_snare = [
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
]
# Hihat on every eighth
drum_notes_bar2_hihat = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes_bar2:
    drums.notes.append(note)
for note in drum_notes_bar2_snare:
    drums.notes.append(note)
for note in drum_notes_bar2_hihat:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
