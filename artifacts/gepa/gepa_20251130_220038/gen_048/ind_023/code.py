
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2: 7th chord on 2 (Ab7)
    pretty_midi.Note(velocity=85, pitch=57, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=85, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.625),  # Db
    pretty_midi.Note(velocity=85, pitch=64, start=2.25, end=2.625),  # Eb

    # Bar 3: 7th chord on 2 (D7)
    pretty_midi.Note(velocity=85, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=85, pitch=52, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=85, pitch=55, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=85, pitch=57, start=3.75, end=4.125),  # A

    # Bar 4: 7th chord on 2 (C7)
    pretty_midi.Note(velocity=85, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=85, pitch=64, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.625),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody - short motif, whisper to cry
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=95, pitch=60, start=2.625, end=3.0),  # C

    # Bar 3: Continue motif
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=95, pitch=65, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.5),  # D

    # Bar 4: Finish motif
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=95, pitch=65, start=5.625, end=6.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 1: Drums only
# Bars 2-4: Full quartet

# Drums in bars 2-4
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)

drums.notes.extend([note for note in [pretty_midi.Note(velocity=90, pitch=36, start=start, end=start + 0.375),
                                     pretty_midi.Note(velocity=90, pitch=36, start=start + 0.75, end=start + 1.125),
                                     pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75),
                                     pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5),
                                     pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
                                     pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
                                     pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
                                     pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5)
                                     ] for bar in range(2, 5) for start in [(1.5 * bar)])


midi.instruments.extend([sax, bass, piano, drums])

midi.write("whisper_to_cry.mid")
