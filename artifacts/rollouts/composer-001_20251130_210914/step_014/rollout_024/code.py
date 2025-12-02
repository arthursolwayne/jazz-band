
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F
# Chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=3.0),  # Ab

    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=4.25, end=4.5),  # F

    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=46, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# F7, Bb7, F7, Bb7
piano_notes = [
    # Bar 2, beat 2 (1.75-2.0)
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),  # F7

    # Bar 2, beat 4 (2.25-2.5)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # Bb7

    # Bar 3, beat 2 (3.25-3.5)
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # F7

    # Bar 3, beat 4 (3.75-4.0)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # Bb7

    # Bar 4, beat 2 (4.75-5.0)
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),  # F7

    # Bar 4, beat 4 (5.25-5.5)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5),  # Bb7
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax motif
# Start with a short phrase, leave it hanging, return to finish
# Use F minor scale with chromatic tension
sax_notes = [
    # Bar 2, beat 1 (1.5-1.75)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # G#
    # Bar 2, beat 3 (2.25-2.5)
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.75),  # F
    # Bar 3, beat 1 (3.0-3.25)
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # F
    # Bar 3, beat 3 (3.75-4.0)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=110, pitch=68, start=4.0, end=4.25),  # G
    # Bar 4, beat 1 (4.5-4.75)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # G#
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # F#
    # Bar 4, beat 3 (5.0-5.25)
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # D
    # Bar 4, beat 4 (5.75-6.0)
    pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(0, 4):
        start_eighth = start + i * 0.375
        pretty_midi.Note(velocity=90, pitch=42, start=start_eighth, end=start_eighth + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
