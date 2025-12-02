
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
    # Hihat on every eighth note
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # F - Gb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),
    # G - Ab (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.625),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=84, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G# - Ab - F (short, expressive, not a scale)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=1.6875, end=1.875),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0625),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.0625, end=2.25),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Sax continues the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=2.4375, end=2.625),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.8125),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=2.8125, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Sax outro, resolves on F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=100, pitch=73, start=3.1875, end=3.375),  # G#
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.5625, end=3.75),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Drums continue the energy
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("4_bar_jazz_intro.mid")
