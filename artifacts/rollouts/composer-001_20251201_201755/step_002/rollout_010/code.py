
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
    # Hihat on every eighth
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
# Bass: Walking line (F2-C2-F2-A2), chromatic approach on C2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.125),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=2.125, end=2.5),   # F2
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.875),   # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chords each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=2.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif - short, singing, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=105, pitch=64, start=1.75, end=2.0),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (Ab2-F2-C2-F2), chromatic approach on F2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.625),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=3.625, end=4.0),   # F2
    pretty_midi.Note(velocity=90, pitch=48, start=4.0, end=4.375),   # F2
]
bass.notes.extend(bass_notes)

# Piano: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.5),  # F#
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),  # A
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation - resolves the first phrase
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=65, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=105, pitch=62, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=105, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=105, pitch=62, start=3.75, end=4.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (Ab2-F2-C2-F2), chromatic approach on F2
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # Ab2
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.125),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=48, start=5.125, end=5.5),   # F2
    pretty_midi.Note(velocity=90, pitch=48, start=5.5, end=5.875),   # F2
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=5.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=5.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=64, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=105, pitch=62, start=4.75, end=5.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
