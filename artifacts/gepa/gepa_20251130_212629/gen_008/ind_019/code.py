
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # E
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
# Bar 2: D7 on beat 2
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=95, pitch=70, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=95, pitch=74, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=95, pitch=76, start=1.875, end=2.0),  # C
    # Bar 3, beat 2
    pretty_midi.Note(velocity=95, pitch=70, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=95, pitch=74, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=95, pitch=76, start=3.375, end=3.5),  # C
    # Bar 4, beat 2
    pretty_midi.Note(velocity=95, pitch=70, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=95, pitch=74, start=4.875, end=5.0),  # A
    pretty_midi.Note(velocity=95, pitch=76, start=4.875, end=5.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: Dante, short motif, start it, leave it hanging, come back and finish it
# Motif: D - Eb - F - Eb (half notes), staggered across bars
sax_notes = [
    # Bar 2: D (half note)
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=2.25),
    # Bar 3: Eb (half note)
    pretty_midi.Note(velocity=105, pitch=64, start=2.25, end=3.0),
    # Bar 4: F - Eb (half notes)
    pretty_midi.Note(velocity=105, pitch=65, start=3.0, end=3.75),
    pretty_midi.Note(velocity=105, pitch=64, start=3.75, end=4.5),
    # Bar 4: F
    pretty_midi.Note(velocity=105, pitch=65, start=4.5, end=5.25),
    # Bar 4: Eb
    pretty_midi.Note(velocity=105, pitch=64, start=5.25, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5),
    # Add to drum notes list
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5),
    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
