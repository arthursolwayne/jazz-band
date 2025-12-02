
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking in Fm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=38, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=39, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),   # F
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - Fm7 on 2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # Bb
    # Bar 3 - Bb7 on 2
    pretty_midi.Note(velocity=100, pitch=43, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # Eb
    # Bar 4 - Fm7 on 2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=39, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - One short motif, make it sing
# Start with F, then Bb, then Eb, leave it hanging on the Bb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=40, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=45, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=39, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=45, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=40, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=45, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=39, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=45, start=2.625, end=3.0)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_intro.mid")
