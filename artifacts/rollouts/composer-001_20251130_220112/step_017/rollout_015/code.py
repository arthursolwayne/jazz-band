
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # D7: G
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # D7: B
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),  # D7: D

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # F7: F
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # F7: Bb
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # F7: E
    pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.375),  # F7: F

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D7: G
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # D7: B
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.875),  # D7: D
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - motif, start it, leave it hanging, come back
# Motif: D - E - C - B (1st bar), then return on D
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=59, start=2.625, end=3.0),  # B

    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # Return to D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=59, start=4.125, end=4.5),  # B

    # Bar 4
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=59, start=5.625, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums in Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.125, end=6.25),
])

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
