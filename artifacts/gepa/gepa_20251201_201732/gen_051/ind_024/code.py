
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]

for note in drums_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approach
bass_notes = [
    # Bar 2: D (D2), chromatic approach to G2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.125),  # D#2
    pretty_midi.Note(velocity=80, pitch=40, start=2.125, end=2.5),   # E2
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.875),   # G2
]

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C#5
]

# Sax: motif starts, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.125), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.5),   # A4
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approach to A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.625),  # G#2
    pretty_midi.Note(velocity=80, pitch=45, start=3.625, end=4.0),   # A2
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.375),   # B2
]

# Piano: Bm7 (B, D, F#, A)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # F#4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A4
]

# Sax: motif returns and resolves
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.625), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.625, end=4.0),   # A4
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.375),   # B4
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approach to D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # B2
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.125),  # C3
    pretty_midi.Note(velocity=80, pitch=49, start=5.125, end=5.5),   # C#3
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.875),   # D3
]

# Piano: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # C#5
]

# Sax: motif returns with variation and ends on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.125), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=5.125, end=5.5),   # A4
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=6.0),     # D4
]

for note in bass_notes:
    bass.notes.append(note)
for note in piano_notes:
    piano.notes.append(note)
for note in sax_notes:
    sax.notes.append(note)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
