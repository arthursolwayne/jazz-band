
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (Root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2 (Chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2 (Fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=2.625, end=3.0),  # F2 (Chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D (MIDI 62)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A (MIDI 69)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F (MIDI 64)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E (MIDI 65)
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0),  # D (MIDI 62)
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G (MIDI 67)
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # A (MIDI 69)
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),  # F2 (Chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),  # D2 (Root)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # G2 (Fifth)
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # Eb2 (Chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Bar 3: G7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G (MIDI 67)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C (MIDI 72)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # Bb (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A (MIDI 69)
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve on G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # Eb2 (Chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # D2 (Root)
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # G2 (Fifth)
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),   # F2 (Chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Bar 4: Cmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0),  # C (MIDI 72)
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=6.0),  # E (MIDI 76)
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=6.0),  # G (MIDI 74)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # Bb (MIDI 71)
]
piano.notes.extend(piano_notes)

# Sax: Resolve motif, end on a strong note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),  # A
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
