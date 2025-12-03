
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=70, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=70, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=70, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=70, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches, roots and fifths
# F - G - A - Bb - C - D - Eb - F - G - A - Bb - C - D - Eb - F - G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=73, start=1.875, end=2.25), # G (fifth)
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.625), # Ab (chromatic)
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # F (root)
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),  # C (fifth)
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.75), # Bb (chromatic)
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125), # C (root)
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # D (fifth)
    pretty_midi.Note(velocity=80, pitch=75, start=4.5, end=4.875),  # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25), # D (root)
    pretty_midi.Note(velocity=80, pitch=78, start=5.25, end=5.625), # F (fifth)
    pretty_midi.Note(velocity=80, pitch=77, start=5.625, end=6.0),  # Gb (chromatic)
    pretty_midi.Note(velocity=80, pitch=78, start=6.0, end=6.375),  # F (root)
    pretty_midi.Note(velocity=80, pitch=80, start=6.375, end=6.75), # G (fifth)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Bb7 (F, Bb, D, Ab)
# Bar 3: Cm7 (C, Eb, G, Bb)
# Bar 4: F7 (F, A, C, Eb)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Ab

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # Bb

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # Eb

    # Bar 4 resolution
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=5.25),   # F
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=5.25),   # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=5.25),   # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.25),   # Ab
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, incomplete, haunting
# F - Ab - C - (rest) - G - Bb - F - Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625), # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25), # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
