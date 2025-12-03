
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: walking line with roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2: Root F (F2), chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.5 + 0.125),
    # Bar 2: Fifth C (C3), chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=1.875 + 0.125),
    # Bar 3: Root F (F2), chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.25 + 0.125),
    # Bar 3: Fifth C (C3), chromatic approach from B
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=2.625 + 0.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),
    # Bar 3: Bbmaj7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=83, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Sax: Bar 2-4
# Motif: F (G), Bb (A), C (B), D (C) - short, singable, leaves it hanging
sax_notes = [
    # Bar 2: F (G) - start on beat 1
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.6875),
    # Bar 2: Bb (A) - start on beat 2
    pretty_midi.Note(velocity=110, pitch=77, start=1.875, end=2.0625),
    # Bar 3: C (B) - start on beat 3
    pretty_midi.Note(velocity=110, pitch=79, start=2.625, end=2.8125),
    # Bar 3: D (C) - start on beat 4
    pretty_midi.Note(velocity=110, pitch=82, start=3.0, end=3.1875),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
