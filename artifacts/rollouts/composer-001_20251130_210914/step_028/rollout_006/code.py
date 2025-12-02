
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

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),   # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=45, start=1.5, end=1.875),  # F7: F, A, C, Eb
    pretty_midi.Note(velocity=95, pitch=48, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=95, pitch=47, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=45, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=95, pitch=48, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=95, pitch=47, start=2.25, end=2.625),  # Eb
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=45, start=3.375, end=3.75),  # F7
    pretty_midi.Note(velocity=95, pitch=48, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=95, pitch=47, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=95, pitch=45, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=95, pitch=48, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=95, pitch=47, start=3.75, end=4.125),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=45, start=4.875, end=5.25),  # F7
    pretty_midi.Note(velocity=95, pitch=48, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=95, pitch=47, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=95, pitch=45, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=95, pitch=48, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=95, pitch=50, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=95, pitch=47, start=5.25, end=5.625),  # Eb
]
piano.notes.extend(piano_notes)

# Saxophone (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=6.0),   # G
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
drum_notes = []
# Kick on 1 and 3
for bar in range(2, 4):
    for beat in [0, 2]:
        start = 1.5 + (bar - 2) * 1.5 + beat * 0.75
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
# Snare on 2 and 4
for bar in range(2, 4):
    for beat in [1, 3]:
        start = 1.5 + (bar - 2) * 1.5 + beat * 0.75
        drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.375))
# Hi-hat on every eighth
for bar in range(2, 4):
    for beat in range(0, 6):
        start = 1.5 + (bar - 2) * 1.5 + beat * 0.375
        drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.375))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
