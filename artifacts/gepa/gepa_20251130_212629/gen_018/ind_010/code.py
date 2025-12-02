
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches, Fm7 -> Bb7 -> Eb7 -> Am7
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=39, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=100, pitch=39, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp for rhythm
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # F7 - Bb
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),  # F7 - Eb
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),  # F7 - Ab
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Eb7 - G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # Eb7 - Bb
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # Eb7 - Eb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # Eb7 - D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Eb7 - G
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=4.875),  # Eb7 - Bb
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # Eb7 - Eb
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # Eb7 - D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
for bar in [2, 3, 4]:
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.1875)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875)
    # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.6875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
