
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # G#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # A#
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.625), # D#
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0)   # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),  # E
    # Bar 3 - B7 (B, D#, F#, A)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),  # A
    # Bar 4 - E7 (E, G#, B, D)
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=89, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Motif starts on beat 2 of bar 2
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.625),  # B
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75),  # B
    # Return and finish
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
