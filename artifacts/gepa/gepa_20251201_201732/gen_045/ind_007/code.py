
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

# Marcus on bass: Walking line in F (F2, Bb2, C3, D3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25), # Bb2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),  # D3

    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # D3
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # F3
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.125), # A3
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),  # Bb3

    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # Bb3
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25), # C4
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D4
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),  # Eb4
]
bass.notes.extend(bass_notes)

# Diane on piano: Open voicings, resolve on last beat of each bar
piano_notes = [
    # Bar 2 - Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875), # C5
    pretty_midi.Note(velocity=100, pitch=73, start=1.5, end=1.875), # E5

    # Bar 3 - F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375), # A4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # Eb5

    # Bar 4 - Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # F4
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875), # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # Eb5
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # B4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # B4

    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # C4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # B4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F4

    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # B4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Hihat on 4

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
