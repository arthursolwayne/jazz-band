
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

# Marcus on bass - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # G#
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=80, pitch=49, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # A#
]

for note in bass_notes:
    bass.notes.append(note)

# Diane on piano - 7th chords on 2 and 4
# F7 on beat 2 of bar 2, Bb7 on beat 2 of bar 3, E7 on beat 2 of bar 4
piano_notes = [
    # F7 (F, A, C, E)
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625),
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125),
    # E7 (E, G#, B, D)
    pretty_midi.Note(velocity=80, pitch=56, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray on drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.999),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante on sax - melody: start with a whisper, build to a cry
sax_notes = [
    # Bar 2: Whisper
    pretty_midi.Note(velocity=60, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=60, pitch=64, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=60, pitch=65, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=60, pitch=62, start=2.625, end=3.0),   # G
    # Bar 3: Build
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # D
    # Bar 4: Cry
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
