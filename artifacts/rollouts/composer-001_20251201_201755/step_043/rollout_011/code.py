
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) - root
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    # Fm7 root movement: D2 -> Ab2 (MIDI 43) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    # G2 (MIDI 43) - fifth
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    # D2 (MIDI 38) - root
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # D (MIDI 67)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Start with a short motif on F (MIDI 53)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=53, start=1.75, end=2.0),
    # Come back and finish it with a chromatic approach to Ab (MIDI 60)
    pretty_midi.Note(velocity=110, pitch=59, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.5),
    # End on Bb (MIDI 62) to add tension
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) - fifth
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    # Fm7 root movement: G2 -> C2 (MIDI 40) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),
    # D2 (MIDI 38) - root
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),
    # G2 (MIDI 43) - fifth
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Am7 (A, C, E, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # A (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # E (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G (MIDI 67)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, unresolved tension
sax_notes = [
    # Continue the unresolved tension with a chromatic approach to Bb (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),
    # Come back and finish it with a chromatic approach to B (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=61, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),
    # End on Bb (MIDI 62) to add tension
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) - root
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    # Fm7 root movement: D2 -> G2 (MIDI 43) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),
    # C2 (MIDI 40) - chromatic approach
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),
    # G2 (MIDI 43) - fifth
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # Ab (MIDI 60)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # C (MIDI 64)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # D (MIDI 67)
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif with a resolution to F (MIDI 53)
sax_notes = [
    # Resolve the tension to F (MIDI 53)
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=53, start=4.75, end=5.0),
    # Add a descending chromatic line to build tension
    pretty_midi.Note(velocity=110, pitch=52, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=51, start=5.25, end=5.5),
    # End on F (MIDI 53) for resolution
    pretty_midi.Note(velocity=110, pitch=53, start=5.5, end=5.75),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
