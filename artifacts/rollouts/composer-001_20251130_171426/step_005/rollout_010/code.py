
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

# Drums in bar 1
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on & 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on & 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on & 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on & 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=48, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=46, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.25),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Drums in bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Hihat on & 1
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Hihat on & 2
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Hihat on & 3
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on & 4
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875)
drums.notes.extend(drum_notes)

# Saxophone (Dante) - Melody in bars 2-4
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
