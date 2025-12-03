
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # F3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # G2 (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # E2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G (Fmaj7 3rd)
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25), # Bb (upper tension)
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.875), # G (return)
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),  # Bb (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # E2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # C (Cm7 root)
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.75), # Eb (Cm7 3rd)
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.375), # C (return)
    pretty_midi.Note(velocity=110, pitch=63, start=4.375, end=4.5),  # Eb (resolve)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # F2 (root)
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25), # A2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625), # Bb2 (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),  # G2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Amaj7 (A, C#, E, G#)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C#
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # G#
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # A (Amaj7 root)
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25), # C# (Amaj7 3rd)
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=5.875), # A (return)
    pretty_midi.Note(velocity=110, pitch=69, start=5.875, end=6.0),  # C# (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
