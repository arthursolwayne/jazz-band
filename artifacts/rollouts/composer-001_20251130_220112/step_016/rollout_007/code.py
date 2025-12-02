
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
# Bass: Walking line in D, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: D - C# - E - F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    # Bar 3: F# - G - A - Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),  # Bb
    # Bar 4: C - D - E - D
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=77, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=4.125),  # C
    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=79, start=4.125, end=4.5),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=80, pitch=79, start=5.625, end=6.0),  # F#
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it
sax_notes = [
    # Bar 2: D (62) on beat 1, F# (72) on beat 2, G (72) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),
    # Bar 3: A (69) on beat 1, Bb (66) on beat 2, C (60) on beat 3
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),
    # Bar 4: D (62) on beat 1, G (72) on beat 2, E (64) on beat 3
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=64, start=6.0, end=6.375),
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Bar 2: Kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Bar 3: Kick on 1 and 3, snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Bar 4: Kick on 1 and 3, snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
]
drums.notes.extend(drum_notes)

# Add hi-hats on every eighth note for all bars
for bar in range(2, 5):
    for i in range(0, 4):
        start = bar * 1.5 + i * 0.375
        end = start + 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dante_moment.mid")
