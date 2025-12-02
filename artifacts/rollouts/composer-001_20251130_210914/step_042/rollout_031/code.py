
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus: walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # Fm7 root
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Fm7 b9
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # Fm7 b7
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Fm7 9
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Fm7 9
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # Fm7 root
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # Fm7 b5
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),  # Fm7 b9
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # Fm7 b9
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.25), # Fm7 b7
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # Fm7 root
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Fm7 9
]
bass.notes.extend(bass_notes)

# Piano - Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=43, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # Bb7
    pretty_midi.Note(velocity=85, pitch=52, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=1.875),  # Ab
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=43, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # Bb7
    pretty_midi.Note(velocity=85, pitch=52, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375),  # Ab
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=43, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),  # Bb7
    pretty_midi.Note(velocity=85, pitch=52, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875),  # Ab
]
piano.notes.extend(piano_notes)

# Sax - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, C (F - Ab - Bb - C)
# Start on bar 2, leave it hanging on Bb, finish it on bar 4
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=43, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=1.875, end=2.0625), # Bb
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=50, start=2.0625, end=2.25), # C
    pretty_midi.Note(velocity=110, pitch=43, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=110, pitch=47, start=2.4375, end=2.625), # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=2.625, end=2.8125), # Bb
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=50, start=2.8125, end=3.0), # C
    pretty_midi.Note(velocity=110, pitch=43, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=3.375, end=3.5625), # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=3.5625, end=3.75), # C
    pretty_midi.Note(velocity=110, pitch=43, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=3.9375, end=4.125), # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=4.125, end=4.3125), # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=4.3125, end=4.5),  # C
    pretty_midi.Note(velocity=110, pitch=43, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=5.0625, end=5.25), # C
    pretty_midi.Note(velocity=110, pitch=43, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=110, pitch=47, start=5.4375, end=5.625), # Ab
    pretty_midi.Note(velocity=110, pitch=48, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=110, pitch=50, start=5.8125, end=6.0),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.0625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.8125, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
