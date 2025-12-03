
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875)    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),   # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),   # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.25),   # G2 on 3
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.5),   # F#2 on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.75),   # G#2 on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0),   # D2 on 2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, one chord each bar
# Bar 2: F7 (F A C E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # F (71)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),  # A (76)
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=3.0),  # C (79)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # E (82)
]
# Bar 3: Bb7 (Bb D F A)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # Bb (67)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # D (72)
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # F (76)
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # A (82)
]
# Bar 4: C7 (C E G B)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C (60)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E (64)
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G (67)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B (71)
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Drums: kick=36, snare=38, hihat=42
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375)    # Hihat on 4
]
drums.notes.extend(drum_notes_bar2)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: Motif (F, G#, Bb, C) — short, singing, with space
sax_notes_bar3 = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F (71)
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75), # G# (74)
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125), # Bb (76)
    pretty_midi.Note(velocity=110, pitch=79, start=4.125, end=4.5),  # C (79)
]
sax.notes.extend(sax_notes_bar3)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43)
bass_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.75),   # D2 on 1
    pretty_midi.Note(velocity=100, pitch=40, start=4.75, end=5.0),   # F2 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=5.0, end=5.25),   # G2 on 3
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.5),   # F#2 on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.75),   # G#2 on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=6.0),   # D2 on 2
]
bass.notes.extend(bass_notes_bar4)

# Piano: Comp on 2 and 4
piano_notes_bar4_comp = [
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Bb (67)
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # D (72)
    pretty_midi.Note(velocity=100, pitch=76, start=5.0, end=5.25),  # F (76)
    pretty_midi.Note(velocity=100, pitch=82, start=5.0, end=5.25),  # A (82)
]
piano.notes.extend(piano_notes_bar4_comp)

# Drums: kick=36, snare=38, hihat=42
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375)    # Hihat on 4
]
drums.notes.extend(drum_notes_bar4)

# Sax: Resolve the motif (F, G#, Bb, C) with a final note on C
sax_notes_bar4 = [
    pretty_midi.Note(velocity=110, pitch=79, start=5.5, end=6.0),  # C (79)
]
sax.notes.extend(sax_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
