
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=80, pitch=70, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # F2
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=78, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.875),  # E
]

# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # Ab
])

# Bar 4: D7 (D, F#, A, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # C
])

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, short motif, one phrase, start it, leave it hanging, come back
# Motif: F - G - C - Bb (start on F at 1.5s, end on Bb at 2.625s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=73, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=78, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=76, start=2.625, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
