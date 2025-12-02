
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=39, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=85, pitch=40, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=85, pitch=41, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=85, pitch=43, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=85, pitch=44, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=85, pitch=45, start=2.75, end=3.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),  # F7: Bb
    pretty_midi.Note(velocity=85, pitch=50, start=1.5, end=1.75),  # F7: D
    pretty_midi.Note(velocity=85, pitch=47, start=1.5, end=1.75),  # F7: F
    pretty_midi.Note(velocity=85, pitch=44, start=1.5, end=1.75),  # F7: A
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5),  # F7: Bb
    pretty_midi.Note(velocity=85, pitch=50, start=2.25, end=2.5),  # F7: D
    pretty_midi.Note(velocity=85, pitch=47, start=2.25, end=2.5),  # F7: F
    pretty_midi.Note(velocity=85, pitch=44, start=2.25, end=2.5),  # F7: A
]

for note in piano_notes:
    piano.notes.append(note)

# Dante on sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=2.75, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: walking line
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=44, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=45, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=85, pitch=47, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=85, pitch=48, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=85, pitch=49, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=85, pitch=50, start=4.25, end=4.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # F7: Bb
    pretty_midi.Note(velocity=85, pitch=50, start=3.0, end=3.25),  # F7: D
    pretty_midi.Note(velocity=85, pitch=47, start=3.0, end=3.25),  # F7: F
    pretty_midi.Note(velocity=85, pitch=44, start=3.0, end=3.25),  # F7: A
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.0),  # F7: Bb
    pretty_midi.Note(velocity=85, pitch=50, start=3.75, end=4.0),  # F7: D
    pretty_midi.Note(velocity=85, pitch=47, start=3.75, end=4.0),  # F7: F
    pretty_midi.Note(velocity=85, pitch=44, start=3.75, end=4.0),  # F7: A
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Continue the motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=58, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=95, pitch=60, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=62, start=4.25, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: walking line
bass_notes = [
    pretty_midi.Note(velocity=85, pitch=50, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=85, pitch=52, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=85, pitch=53, start=5.0, end=5.25),  # G#
    pretty_midi.Note(velocity=85, pitch=55, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=85, pitch=57, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=85, pitch=58, start=5.75, end=6.0),  # B
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),  # F7: Bb
    pretty_midi.Note(velocity=85, pitch=50, start=4.5, end=4.75),  # F7: D
    pretty_midi.Note(velocity=85, pitch=47, start=4.5, end=4.75),  # F7: F
    pretty_midi.Note(velocity=85, pitch=44, start=4.5, end=4.75),  # F7: A
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.5),  # F7: Bb
    pretty_midi.Note(velocity=85, pitch=50, start=5.25, end=5.5),  # F7: D
    pretty_midi.Note(velocity=85, pitch=47, start=5.25, end=5.5),  # F7: F
    pretty_midi.Note(velocity=85, pitch=44, start=5.25, end=5.5),  # F7: A
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Finish the motif, a cry that builds
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=58, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=95, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=5.75, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
