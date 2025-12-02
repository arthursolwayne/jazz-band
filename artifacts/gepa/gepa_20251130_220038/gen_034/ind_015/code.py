
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
    # Hihat on every eighth
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Walking line in F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # Gb
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),  # C
    # Bar 3: F7 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),  # C
    # Bar 4: F7 on 2
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - Melody
# Bar 2: 4-note motif starting on F
# F (71), Ab (70), G (72), F (71)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=70, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),
    # Bar 3: Repeat the motif, but with a slight variation
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),
    # Bar 4: Return to the motif, but leave it hanging
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=70, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_moment.mid")
