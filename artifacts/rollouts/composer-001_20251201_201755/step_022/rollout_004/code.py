
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F root (F2, MIDI 53)
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.75),
    # Bb (F2 + 4, MIDI 57) with chromatic approach from B (MIDI 58)
    pretty_midi.Note(velocity=80, pitch=58, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=57, start=1.875, end=2.125),
    # C (F2 + 7, MIDI 60) with chromatic approach from Bb (MIDI 57)
    pretty_midi.Note(velocity=80, pitch=57, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # A (F2 + 3, MIDI 58) with chromatic approach from G# (MIDI 57)
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=58, start=3.125, end=3.375),
    # D (F2 + 6, MIDI 62) with chromatic approach from C# (MIDI 61)
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75),
    # G (F2 + 9, MIDI 67) with chromatic approach from F# (MIDI 66)
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=67, start=3.875, end=4.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=110, pitch=73, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C (F2 + 7, MIDI 60) with chromatic approach from B (MIDI 59)
    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=60, start=4.625, end=4.875),
    # F (root, MIDI 53) with chromatic approach from E (MIDI 52)
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25),
    # G (F2 + 9, MIDI 67) with chromatic approach from F# (MIDI 66)
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=67, start=5.375, end=5.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=110, pitch=73, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 3-4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
