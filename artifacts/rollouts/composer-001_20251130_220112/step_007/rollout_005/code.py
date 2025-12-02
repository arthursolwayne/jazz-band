
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 1.5, note_number=42)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75, note_number=42)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125, note_number=42)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5, note_number=42)
    drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),  # Bb

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: D7 (F# - D - G - C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.25),  # F#

    # Bar 3: rest
    # Bar 4: G7 (B - G - D - F#)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=5.25),  # F#
]
piano.notes.extend(piano_notes)

# Drums: same pattern for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    hihat = pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 1.5, note_number=42)
    hihat2 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75, note_number=42)
    hihat3 = pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125, note_number=42)
    hihat4 = pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5, note_number=42)
    drums.notes.extend([kick, snare, hihat, hihat2, hihat3, hihat4])

# Sax solo: one short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
