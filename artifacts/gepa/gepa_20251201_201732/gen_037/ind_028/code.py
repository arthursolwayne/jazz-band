
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # C3 (fifth of F)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # F (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, D#, F (G#), E, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.625),  # F (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=55, start=1.625, end=1.75),  # D#
    pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),   # G#
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=2.125, end=2.25),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # C3 (fifth of F)
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # C#3
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # D (MIDI 52)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
# Motif: F, D#, F (G#), E, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.125),  # F (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=55, start=3.125, end=3.25),  # D#
    pretty_midi.Note(velocity=100, pitch=58, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),   # G#
    pretty_midi.Note(velocity=100, pitch=59, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=3.625, end=3.75),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=40, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # G#2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # Bb2 (chromatic approach to C3)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C E G Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
# Motif: F, D#, F (G#), E, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.625),  # F (MIDI 58)
    pretty_midi.Note(velocity=100, pitch=55, start=4.625, end=4.75),  # D#
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),   # G#
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.125),  # E
    pretty_midi.Note(velocity=100, pitch=58, start=5.125, end=5.25),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
