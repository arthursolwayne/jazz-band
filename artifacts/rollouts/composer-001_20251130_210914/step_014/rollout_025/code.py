
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0), # A
]
bass.notes.extend(bass_notes)

# Diane - Comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375), # F7
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # F7
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875),
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375),
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125),
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.6875),

drums.notes.extend(drum_notes)

# Dante - Sax motif
sax_notes = [
    # Bar 2, 1st beat: Start with a descending motif
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.0625, end=2.25), # F
    # Bar 3: Leave it hanging, return with the same motif
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.5625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.5625, end=3.75), # F
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875), # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25), # F
    # Repeat the motif with a twist
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=100, pitch=66, start=5.4375, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0), # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
