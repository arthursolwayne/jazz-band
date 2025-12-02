
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line (F2-C3-G3-A3-C4), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=78, start=1.875, end=2.25), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=100, pitch=82, start=2.625, end=3.0),  # A2
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=85, start=3.375, end=3.75), # B2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=87, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=100, pitch=89, start=4.125, end=4.5),  # D3
    pretty_midi.Note(velocity=100, pitch=91, start=4.5, end=4.875),  # E3
    pretty_midi.Note(velocity=100, pitch=92, start=4.875, end=5.25), # F3
    pretty_midi.Note(velocity=100, pitch=94, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=100, pitch=96, start=5.625, end=6.0),  # A3
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, resolve on the last bar
# Bar 2: F7 (F A C E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # E
]

# Bar 3: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=75, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.625),  # Bb
])

# Bar 4: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.375),  # F
])

# Bar 4 resolution: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # B
])

piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing.
# Start on F, move to Bb, then to D, leave it hanging on the 4th beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=86, start=3.375, end=3.75),  # D (echo)
    pretty_midi.Note(velocity=100, pitch=86, start=4.125, end=4.5),  # D (echo)
    pretty_midi.Note(velocity=100, pitch=86, start=4.875, end=5.25),  # D (echo)
]

sax.notes.extend(sax_notes)

# Drums continue in bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 2
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_introduction.mid")
