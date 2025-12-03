
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

# Bar 1: Add to drum instrument
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass (Marcus) - walking line with chromatic approaches
# D2-G2 (MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # E2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, resolve on the last bar
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax (Dante) - short motif, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # E2
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar
# Bar 3: Dm7 -> G7 -> Cmaj7
# Dm7 (D4-F4-A4-C5), G7 (G4-B4-D5-F5), Cmaj7 (C4-E4-G4-B4)
piano_notes = [
    # Dm7
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.375),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # C5
    # G7
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),  # B4
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),  # D5
    pretty_midi.Note(velocity=110, pitch=76, start=3.375, end=3.75),  # F5
    # Cmaj7
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),  # B4
]
piano.notes.extend(piano_notes)

# Sax (Dante) - continue the motif, leave it hanging again
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5),
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

# Bass (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D3
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625),  # D#3
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # F3
]
bass.notes.extend(bass_notes)

# Piano (Diane) - open voicings, different chord each bar
# Bar 4: Dm7 -> G7 -> Cmaj7 -> Dm7
piano_notes = [
    # Dm7
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),  # C5
]
piano.notes.extend(piano_notes)

# Sax (Dante) - finish the motif, leave it open
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
