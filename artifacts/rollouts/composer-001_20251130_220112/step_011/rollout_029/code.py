
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5), # Eb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0), # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875), # F7 3rd
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875), # F7 5th
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875), # F7 7th
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875), # F7 9th
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375), # F7 3rd
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375), # F7 5th
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375), # F7 7th
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375), # F7 9th
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875), # F7 3rd
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875), # F7 5th
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875), # F7 7th
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875), # F7 9th
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875), # Ab
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0), # G
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_moment.mid")
