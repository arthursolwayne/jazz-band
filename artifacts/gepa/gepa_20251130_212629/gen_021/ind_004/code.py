
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
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),   # Snare on 4
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=1.5)    # Hihat on every eighth
]
drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# F7 chord: F, A, C, E, Bb
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=70, pitch=66, start=1.875, end=2.25), # Gb (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=67, start=2.25, end=2.625), # G (upward motion)
    pretty_midi.Note(velocity=70, pitch=66, start=2.625, end=3.0),  # Gb (back down)
    pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=70, pitch=64, start=3.375, end=3.75), # Eb (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=65, start=3.75, end=4.125), # F (root)
    pretty_midi.Note(velocity=70, pitch=67, start=4.125, end=4.5),  # G (upward motion)
    pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.875),  # A (next chord)
    pretty_midi.Note(velocity=70, pitch=68, start=4.875, end=5.25), # Ab (chromatic approach)
    pretty_midi.Note(velocity=70, pitch=67, start=5.25, end=5.625), # G (back down)
    pretty_midi.Note(velocity=70, pitch=69, start=5.625, end=6.0),  # A (final chord)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E, Bb
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # C (F7)
    pretty_midi.Note(velocity=80, pitch=74, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=77, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=79, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # C (F7)
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=77, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=79, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # C (F7)
    pretty_midi.Note(velocity=80, pitch=74, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=77, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # C (F7)
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=77, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=79, start=4.875, end=5.25),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F F# G F (Motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),   # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),   # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),   # F
]
sax.notes.extend(sax_notes)

# Add hi-hat fills with subtle variations
hi_hat_notes = [
    pretty_midi.Note(velocity=50, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=50, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=50, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=50, pitch=42, start=4.5, end=4.625)
]
drums.notes.extend(hi_hat_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
