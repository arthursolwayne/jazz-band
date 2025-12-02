
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking in Fm (F, Eb, D, C), chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Fm7 on 1, Bbm7 on 2, Eb7 on 3, Abm7 on 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875), # G
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=80, pitch=58, start=2.25, end=2.625), # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375), # Eb
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=55, start=3.0, end=3.375), # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375), # Eb
    # Bar 4 (second half)
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875), # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875), # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875), # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Your motif (start on beat 2 of bar 2)
# F, Ab, Bb, D (Fm7 chord, implied)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.125), # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.125, end=2.375), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),    # F (return)
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # D
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    drum_notes = [
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75),
        pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5),
        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125),
        pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5),
    ]
    for note in drum_notes:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
