
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375),  # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # C#
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F7 - D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F7 - Eb
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F7 - D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F7 - Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # snare on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # snare on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # snare on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
