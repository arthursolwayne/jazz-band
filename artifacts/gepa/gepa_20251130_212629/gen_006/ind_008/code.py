
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

# Bass line: Marcus
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=46, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=48, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=51, start=2.75, end=3.0),  # A#
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=100, pitch=51, start=3.5, end=3.75),  # A#
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=49, start=4.0, end=4.25),  # G#
    pretty_midi.Note(velocity=100, pitch=48, start=4.25, end=4.5),  # G
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=46, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=44, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=43, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # F7
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # F7
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # F7
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # F7
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Sax: Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A
    
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]

# Bar 3 (3.0 - 4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.375), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 4
])

# Bar 4 (4.5 - 6.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),  # Hihat on 4
])

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
