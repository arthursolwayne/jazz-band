
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line (roots and fifths with chromatic approaches)
# F7 -> Bb7 -> C7 -> E7
bass_notes = [
    # Bar 2 (F7)
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=75, start=1.6875, end=1.875), # C3
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.0),   # G2
    pretty_midi.Note(velocity=80, pitch=70, start=2.0, end=2.1875),  # F2

    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=80, pitch=65, start=2.1875, end=2.375),  # Bb2
    pretty_midi.Note(velocity=80, pitch=70, start=2.375, end=2.5625), # F3
    pretty_midi.Note(velocity=80, pitch=66, start=2.5625, end=2.75),  # Bb2
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=2.9375),  # Bb2

    # Bar 4 (C7)
    pretty_midi.Note(velocity=80, pitch=60, start=2.9375, end=3.125),  # C2
    pretty_midi.Note(velocity=80, pitch=65, start=3.125, end=3.3125), # G3
    pretty_midi.Note(velocity=80, pitch=62, start=3.3125, end=3.5),   # D2
    pretty_midi.Note(velocity=80, pitch=60, start=3.5, end=3.6875),   # C2

    # Bar 5 (E7)
    pretty_midi.Note(velocity=80, pitch=64, start=3.6875, end=3.875),  # E2
    pretty_midi.Note(velocity=80, pitch=69, start=3.875, end=4.0625), # B3
    pretty_midi.Note(velocity=80, pitch=66, start=4.0625, end=4.25),  # C#2
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.4375),  # E2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F A C E)
# Bar 3: Bb7 (Bb D F A)
# Bar 4: C7 (C E G B)
# Bar 5: E7 (E G# B D)
piano_notes = [
    # Bar 2 (F7)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0),  # C4
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=2.0),  # E4

    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.5),  # D4
    pretty_midi.Note(velocity=100, pitch=75, start=2.0, end=2.5),  # F4
    pretty_midi.Note(velocity=100, pitch=78, start=2.0, end=2.5),  # A4

    # Bar 4 (C7)
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # B4

    # Bar 5 (E7)
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.5),  # E4
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.5),  # G#4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.5),  # D4
]
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # F3
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # A3
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # F3
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),  # A3
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # F3
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hats
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend([note for note in drum_notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
