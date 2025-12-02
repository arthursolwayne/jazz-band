
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in F, chromatic approaches, never same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # G#

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # C

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),  # F
]

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # F7 - C

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F7 - C

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # F7 - C
]

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # E

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # E

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # F#
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E
]

# Drums: Full bar (1.5 - 6.0s)
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)

# Add notes to instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write("jazz_intro.mid")
