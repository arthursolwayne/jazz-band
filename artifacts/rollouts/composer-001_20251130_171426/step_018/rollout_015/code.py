
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 - 1.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
# Fm7 chord: F, Ab, C, Eb
# Walking bass line in Fm
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25), # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D (chromatic)
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=3.0),  # C (3rd)

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75), # A (chromatic)
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125), # G (chromatic)
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),  # F (root)

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=56, start=4.5, end=4.875),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25), # D (chromatic)
    pretty_midi.Note(velocity=100, pitch=54, start=5.25, end=5.625), # C (chromatic)
    pretty_midi.Note(velocity=100, pitch=53, start=5.625, end=6.0),  # Bb (chromatic)
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4. Fm7, Bbm7
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # Eb

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75), # Ab

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # Eb
]
piano.notes.extend(piano_notes)

# Dante: Saxophone. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, C, Eb (Fm7) on the 1st beat, then leave it hanging with a trill or run
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=82, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=80, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=87, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=110, pitch=84, start=2.625, end=3.0),  # Eb

    # Bar 3 (3.0 - 4.5s) - leave it hanging
    pretty_midi.Note(velocity=110, pitch=84, start=3.0, end=3.375),  # Eb (hold)
    pretty_midi.Note(velocity=110, pitch=85, start=3.375, end=3.75), # E (trill)
    pretty_midi.Note(velocity=110, pitch=84, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=110, pitch=85, start=4.125, end=4.5),  # E

    # Bar 4 (4.5 - 6.0s) - come back and finish it
    pretty_midi.Note(velocity=110, pitch=82, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=80, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=110, pitch=87, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=110, pitch=84, start=5.625, end=6.0),  # Eb
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
