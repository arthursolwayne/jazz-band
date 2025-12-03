
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm (F, Ab, D, C), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (D2), Ab (D3), D (F#2), C (C2)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=36, start=2.625, end=3.0),  # C
    # Bar 3: Gb (D3) chromatic approach to F, F (D2), Bb (D2), E (D2)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Gb
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=37, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # E
    # Bar 4: F (D2), Ab (D3), D (F#2), C (C2)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last chord of each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
# Bar 3: Gbm7 (Gb, Bb, D, F)
# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875), # F (F4)
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=1.875), # Ab (Ab3)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875), # C (C4)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875), # Eb (Eb4)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375), # Gb (Gb4)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # Bb (Bb3)
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375), # D (D4)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375), # F (F4)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875), # F (F4)
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875), # Ab (Ab3)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875), # C (C4)
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875), # Eb (Eb4)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F, Ab, A, F (descending)
# Legend: F = 65, Ab = 61, A = 69, F = 65
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25), # A
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5), # F
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75), # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0), # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5), # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5)

drums.notes.extend([

])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
