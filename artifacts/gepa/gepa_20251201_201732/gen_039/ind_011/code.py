
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 2
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # F#7
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25), # A7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb7
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # F#7
]

sax.notes.extend(sax_notes)

# Bass: Walking line (Fm)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=35, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=34, start=2.25, end=2.625),  # Eb2
    pretty_midi.Note(velocity=90, pitch=33, start=2.625, end=3.0),   # D2
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=51, start=1.5, end=1.875),  # Ab4
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875),  # Eb5
]

# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F5
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625), # Ab5
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # Eb5
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),  # Bb5
])

piano.notes.extend(piano_notes)

# Bar 2: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 3: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 4: Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

drums.notes.extend(drum_notes)

# Bar 3: Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb7
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # A7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # Bb7
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75),  # F#7
]

sax.notes.extend(sax_notes)

# Bar 4: Sax
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),   # F#7
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Bb7
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # A7
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),   # F#7
]

sax.notes.extend(sax_notes)

# Bar 3: Bass
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # Bb2
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # D3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),   # C3
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Bb2
]

bass.notes.extend(bass_notes)

# Bar 4: Bass
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),   # D3
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # Bb2
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # Eb3
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # C3
]

bass.notes.extend(bass_notes)

# Bar 3: Piano
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625),  # Bb4
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.625),  # F5
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.625),  # Ab5
]

piano.notes.extend(piano_notes)

# Bar 4: Piano
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),   # C5
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),   # Eb5
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.375),   # G5
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.375),   # Bb5
]

piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
