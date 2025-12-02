
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=95, pitch=46, start=1.5, end=2.0),  # F7: F, A, C, E♭
    pretty_midi.Note(velocity=95, pitch=53, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=95, pitch=54, start=1.5, end=2.0),  # E♭
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=95, pitch=46, start=3.0, end=3.5),  # F7
    pretty_midi.Note(velocity=95, pitch=53, start=3.0, end=3.5),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=95, pitch=54, start=3.0, end=3.5),  # E♭
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=95, pitch=46, start=4.5, end=5.0),  # F7
    pretty_midi.Note(velocity=95, pitch=53, start=4.5, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=95, pitch=54, start=4.5, end=5.0),  # E♭
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625)
    # Hi-hat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)

# Sax (Dante)
# Short motif: F - G - F - E♭
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0625, end=2.25),  # E♭
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=2.8125, end=3.0),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.1875),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375), # E♭
    # Finish the motif
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.3125),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=4.3125, end=4.5),   # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.6875),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875)  # E♭
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
