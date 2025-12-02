
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bars 2-4 (1.5 - 6.0s)

# Marcus: Walking line in Fm
bass_notes = [
    # Fm root (F) on beat 1
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),
    # Bb on "and" of 1
    pretty_midi.Note(velocity=80, pitch=68, start=1.875, end=2.125),
    # Ab on beat 2
    pretty_midi.Note(velocity=80, pitch=67, start=2.125, end=2.5),
    # D on "and" of 2
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    # F on beat 3
    pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=3.125),
    # Bb on "and" of 3
    pretty_midi.Note(velocity=80, pitch=68, start=3.125, end=3.375),
    # Ab on beat 4
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),
    # D on "and" of 4
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),
    # F on beat 1
    pretty_midi.Note(velocity=80, pitch=71, start=4.0, end=4.375),
    # Bb on "and" of 1
    pretty_midi.Note(velocity=80, pitch=68, start=4.375, end=4.625),
    # Ab on beat 2
    pretty_midi.Note(velocity=80, pitch=67, start=4.625, end=5.0),
    # D on "and" of 2
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),
    # F on beat 3
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),
    # Bb on "and" of 3
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=5.875),
    # Ab on beat 4
    pretty_midi.Note(velocity=80, pitch=67, start=5.875, end=6.25),
    # D on "and" of 4
    pretty_midi.Note(velocity=80, pitch=64, start=6.25, end=6.5),
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on beat 2 (bar 2)
    pretty_midi.Note(velocity=100, pitch=71, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=68, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=64, start=2.125, end=2.5),
    # Fm7 on beat 4 (bar 2)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),
    # Fm7 on beat 2 (bar 3)
    pretty_midi.Note(velocity=100, pitch=71, start=4.625, end=5.0),
    pretty_midi.Note(velocity=90, pitch=68, start=4.625, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=4.625, end=5.0),
    # Fm7 on beat 4 (bar 3)
    pretty_midi.Note(velocity=100, pitch=71, start=5.875, end=6.25),
    pretty_midi.Note(velocity=90, pitch=68, start=5.875, end=6.25),
    pretty_midi.Note(velocity=90, pitch=67, start=5.875, end=6.25),
    pretty_midi.Note(velocity=90, pitch=64, start=5.875, end=6.25),
]
piano.notes.extend(piano_notes)

# Dante: saxophone motif (start at bar 2)
sax_notes = [
    # Start with F (71), then Ab (67), then Bb (68), then F (71)
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=68, start=2.125, end=2.5),
    pretty_midi.Note(velocity=110, pitch=71, start=2.5, end=2.75),
    # Leave it hanging, come back in bar 3
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.375),
    pretty_midi.Note(velocity=110, pitch=67, start=4.375, end=4.625),
    pretty_midi.Note(velocity=110, pitch=68, start=4.625, end=5.0),
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25),
    # Finish the motif in bar 4
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=68, start=5.875, end=6.25),
    pretty_midi.Note(velocity=110, pitch=71, start=6.25, end=6.5),
]
sax.notes.extend(sax_notes)

# Drums in bars 2-4
# Kick on 1 and 3
for bar in [2, 3, 4]:
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in [2, 3, 4]:
    start = 1.5 + (bar - 2) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in [2, 3, 4]:
    start = 1.5 + (bar - 2) * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
