
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D (D - C# - B - A)
# 1.5 - 3.0s (bar 2)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625), # B
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=3.0),  # A
    # Bar 3: D - F# - E - D
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4: D - C# - B - A
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.25), # C#
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625), # B
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Bar 2: D7 on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25), # C#
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # C#
    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25), # C#
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Play the motif
# D (62) - F# (64) - B (67) - D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25), # D
    # Bar 3: Silence and build
    # No sax until 2.625
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.8125, end=3.0), # B
    # Bar 4: Continue the motif with variation
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.9375, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.3125), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.3125, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875), # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.0625, end=5.25), # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375), # F#
    pretty_midi.Note(velocity=100, pitch=62, start=5.4375, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125), # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.8125, end=6.0), # F#
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
