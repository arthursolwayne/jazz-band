
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),   # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625), # G2
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, resolve on the last beat
piano_notes = [
    # Bar 2: Fmaj7
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # E5
    # Bar 3: Bb7
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=3.0),  # Bb3
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # Ab4
    # Bar 4: C7
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=4.0),  # C4
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=4.0),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),  # E4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax: motif (F, Bb, D, F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F5
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # F5
    # Repeat motif
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.875),  # F5
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.25), # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.625), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=5.0),  # F5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),    # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # Hihat on 1-2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
