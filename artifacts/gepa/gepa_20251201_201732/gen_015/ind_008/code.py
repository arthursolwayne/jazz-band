
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

# Bass: Walking line in Fm (F2, Ab2, Bb2, Db2, etc.)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Ab2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # Bb2
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),  # Db2

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=3.375),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),  # Bb2

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),  # Bb2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last beat
piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=1.875),  # Db

    # Bar 3: Ab7 (Ab, C, Db, F)
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F

    # Bar 4: Bb7 (Bb, D, Eb, F)
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif starts on beat 1 of bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # A
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('jazz_intro.mid')
