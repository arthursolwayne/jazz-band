
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

# Bar 2: Full ensemble (1.5 - 3.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0),   # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),   # D4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 3: G7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=110, pitch=70, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),   # G4
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full ensemble (4.5 - 6.0s)

# Bass: Marcus - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # D2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane - open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=6.0),  # E4
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante - finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=110, pitch=58, start=5.625, end=6.0),   # B3
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
