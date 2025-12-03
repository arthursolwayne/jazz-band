
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approach
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=39, start=2.125, end=2.5),
    pretty_midi.Note(velocity=90, pitch=40, start=2.5, end=2.875),
    # Bar 3: G2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=2.875, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=44, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=45, start=3.875, end=4.25),
    # Bar 4: C2 (bass) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=36, start=4.25, end=4.625),
    pretty_midi.Note(velocity=90, pitch=35, start=4.625, end=4.875),
    pretty_midi.Note(velocity=90, pitch=37, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C
]
# Bar 3: G7 (G B D F)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # F
]
# Bar 4: Cm7 (C Eb G Bb)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (E) F A (D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),  # A
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=3.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
# midi.write disabled
