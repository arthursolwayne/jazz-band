
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.5),   # Db
    pretty_midi.Note(velocity=80, pitch=81, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=82, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=84, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=85, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.625),   # F7
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=69, start=3.75, end=4.125),   # F7
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=85, pitch=69, start=5.25, end=5.625),   # F7
    pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=85, pitch=76, start=5.25, end=5.625),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),   # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: continue filling the bar
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]

for note in drum_notes_bar2:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
