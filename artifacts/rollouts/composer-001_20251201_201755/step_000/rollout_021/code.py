
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875)   # Snare on 4 (out of bar)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (MIDI 53) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2 on 1
    pretty_midi.Note(velocity=100, pitch=54, start=1.875, end=2.25), # G2 on 2
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Eb2 on 3
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),  # F2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (MIDI 71)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif - E (MIDI 64), G (MIDI 67), F (MIDI 65)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # E (leave it hanging)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Bb2 (MIDI 50) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.375),  # Bb2 on 1
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125), # A2 on 3
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # Bb2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Ab7 (Ab, C, Eb, G)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif, finish the phrase
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # E
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 57) walking line with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # D2 on 1
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25), # Eb2 on 2
    pretty_midi.Note(velocity=100, pitch=56, start=5.25, end=5.625), # C2 on 3
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),  # D2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Bbm7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Repeat motif with slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)   # Snare on 4 (out of bar)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
