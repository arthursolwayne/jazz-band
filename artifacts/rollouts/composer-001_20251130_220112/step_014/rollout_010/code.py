
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25), # Gb (chromatic)
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),  # Eb (3rd)
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),  # F (4th)
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # Gb (5th)
    pretty_midi.Note(velocity=80, pitch=37, start=3.375, end=3.75), # D (chromatic)
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125), # Eb (octave)
    pretty_midi.Note(velocity=80, pitch=39, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=80, pitch=36, start=4.875, end=5.25), # C (chromatic)
    pretty_midi.Note(velocity=80, pitch=37, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0)
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # F7: F
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625), # D
    # Bar 3 (3.0-4.5)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.125), # D
    # Bar 4 (4.5-6.0)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Gb - Eb - F (start), then F - Gb (end)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=41, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),   # Gb
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=41, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: Fill the bar
# Bar 2 (1.5-3.0)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),  # Hihat on 4
]
# Bar 3 (3.0-4.5)
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),  # Hihat on 4
]
# Bar 4 (4.5-6.0)
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.1875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
