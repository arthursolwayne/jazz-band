
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # C

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # C

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75), # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75), # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75), # Ab

    # Bar 3 (3.0 - 4.5s) - Bb7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25), # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25), # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25), # Db

    # Bar 4 (4.5 - 6.0s) - Cm7
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75), # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75), # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (One short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
# Fm scale: F, Gb, Ab, Bb, B, Db, E
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # F (leave hanging)
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.append(kick1)
    drums.notes.append(kick2)

# Snare on 2 and 4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.append(snare1)
    drums.notes.append(snare2)

# Hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + (i * 0.375), end=start + (i * 0.375) + 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
