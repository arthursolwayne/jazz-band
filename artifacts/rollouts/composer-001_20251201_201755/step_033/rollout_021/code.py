
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # F2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # A2
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # G2

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # F2
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # A2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # G2

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # F2
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # A2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s): Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5

    # Bar 3 (3.0 - 4.5s): Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4

    # Bar 4 (4.5 - 6.0s): Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.6875),  # E5
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.875), # D5
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # C5
    pretty_midi.Note(velocity=110, pitch=71, start=2.0625, end=2.25),  # E5

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.1875),  # D5
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375), # C5
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625), # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.75),  # C5

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.6875),  # D5
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875), # C5
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625), # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),    # Snare on 4
]
for i in range(2):
    for note in drum_notes:
        new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + i * 1.5, note.end + i * 1.5)
        drums.notes.append(new_note)

# Hi-hats on every eighth
for i in range(3):
    for j in range(8):
        start = 1.5 + i * 1.5 + j * 0.1875
        end = start + 0.1875
        if j % 2 == 0:
            velocity = 80
        else:
            velocity = 70
        drums.notes.append(pretty_midi.Note(velocity, 42, start, end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
