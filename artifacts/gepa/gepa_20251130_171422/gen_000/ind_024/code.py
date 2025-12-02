
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in Fm with chromatic approaches
# Fm: F, Ab, D, C
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),  # F3
    pretty_midi.Note(velocity=90, pitch=63, start=1.6875, end=1.875),  # Eb3
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0625),  # D3
    pretty_midi.Note(velocity=90, pitch=60, start=2.0625, end=2.25),  # C3
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),  # F3
    pretty_midi.Note(velocity=90, pitch=65, start=3.1875, end=3.375),  # F#3 (chromatic)
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.5625),  # Eb3
    pretty_midi.Note(velocity=90, pitch=62, start=3.5625, end=3.75),  # D3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.6875),  # F3
    pretty_midi.Note(velocity=90, pitch=63, start=4.6875, end=4.875),  # Eb3
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0625),  # D3
    pretty_midi.Note(velocity=90, pitch=60, start=5.0625, end=5.25),  # C3
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords comping on 2 and 4
# Fm7 = F Ab C Eb
# Bbm7 = Bb D F Ab
# Eb7 = Eb G Bb D
# Ab7 = Ab C Eb G
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),  # F3
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # Ab3
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875),  # C3
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),  # Eb3
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # F3
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # Ab3
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375),  # C3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # Eb3
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=61, start=3.25, end=3.375),  # Bb3
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375),  # D3
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # F3
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),  # Ab3
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=3.875),  # Bb3
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875),  # D3
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),  # F3
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),  # Ab3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=4.875),  # Eb3
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=4.875),  # G3
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875),  # Bb3
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.375),  # Eb3
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),  # G3
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375),  # Bb3
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375),  # D4
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Melody in Fm, short motif, make it sing
# Fm scale: F, Gb, Ab, A, Bb, C, Db
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F3
    pretty_midi.Note(velocity=100, pitch=68, start=1.6875, end=1.875),  # A3
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0625),  # C3
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.25),  # F3
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),  # Ab3
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.375),  # Bb3
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625),  # F3
    pretty_midi.Note(velocity=100, pitch=68, start=3.5625, end=3.75),  # A3
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F3
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875),  # Bb3
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625),  # Ab3
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25),  # F3
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.4375),  # C3
]
sax.notes.extend(sax_notes)

# Drums (Bar 2-4) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_introduction.mid")
