
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus on bass: walking line (D2-G2, MIDI 38-43)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),  # D2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),   # F2 on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),   # A2 on 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5),   # Bb2 on 4
]

# Diane on piano: open voicings, resolve on last bar
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=2.0),  # Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=2.0),
    pretty_midi.Note(velocity=95, pitch=65, start=2.0, end=2.5),  # G7 (G-B-D-F)
    pretty_midi.Note(velocity=95, pitch=69, start=2.0, end=2.5),
    pretty_midi.Note(velocity=95, pitch=71, start=2.0, end=2.5),
    pretty_midi.Note(velocity=95, pitch=73, start=2.0, end=2.5),
    pretty_midi.Note(velocity=95, pitch=67, start=2.5, end=3.0),  # Cmaj7 (C-E-G-B)
    pretty_midi.Note(velocity=95, pitch=72, start=2.5, end=3.0),
    pretty_midi.Note(velocity=95, pitch=74, start=2.5, end=3.0),
    pretty_midi.Note(velocity=95, pitch=76, start=2.5, end=3.0),
]

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),   # Snare on 4
]

for note in drum_notes_bar2:
    drums.notes.append(note)

# Dante on sax: motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),   # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),   # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=3.0),    # E4
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus on bass: walking line (D2-G2, MIDI 38-43)
bass_notes_bar3 = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.25),  # Bb2 on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.25, end=3.5),   # D2 on 2
    pretty_midi.Note(velocity=90, pitch=40, start=3.5, end=3.75),   # F2 on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),   # A2 on 4
]

# Diane on piano: open voicings, resolve on last bar
piano_notes_bar3 = [
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.5),  # G7 (G-B-D-F)
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.5),
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.5),
    pretty_midi.Note(velocity=95, pitch=73, start=3.0, end=3.5),
    pretty_midi.Note(velocity=95, pitch=67, start=3.5, end=4.0),  # Cmaj7 (C-E-G-B)
    pretty_midi.Note(velocity=95, pitch=72, start=3.5, end=4.0),
    pretty_midi.Note(velocity=95, pitch=74, start=3.5, end=4.0),
    pretty_midi.Note(velocity=95, pitch=76, start=3.5, end=4.0),
]

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.375, end=4.5),   # Snare on 4
]

for note in drum_notes_bar3:
    drums.notes.append(note)

# Dante on sax: continue motif
sax_notes_bar3 = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),   # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),   # E4
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.5),    # G4 (hang)
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus on bass: walking line (D2-G2, MIDI 38-43)
bass_notes_bar4 = [
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.75),  # A2 on 1
    pretty_midi.Note(velocity=90, pitch=43, start=4.75, end=5.0),   # Bb2 on 2
    pretty_midi.Note(velocity=90, pitch=38, start=5.0, end=5.25),   # D2 on 3
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.5),   # F2 on 4
]

# Diane on piano: open voicings, resolve on last bar
piano_notes_bar4 = [
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=5.0),  # Cmaj7 (C-E-G-B)
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=5.0),
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=5.0),
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=5.0),
    pretty_midi.Note(velocity=95, pitch=65, start=5.0, end=5.5),  # G7 (G-B-D-F)
    pretty_midi.Note(velocity=95, pitch=69, start=5.0, end=5.5),
    pretty_midi.Note(velocity=95, pitch=71, start=5.0, end=5.5),
    pretty_midi.Note(velocity=95, pitch=73, start=5.0, end=5.5),
]

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0),   # Snare on 4
]

for note in drum_notes_bar4:
    drums.notes.append(note)

# Dante on sax: finish motif
sax_notes_bar4 = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),   # G4
    pretty_midi.Note(velocity=110, pitch=69, start=5.0, end=5.25),   # A4
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.5),   # G4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=6.0),    # E4
]

# Add all notes to instruments
for note in bass_notes:
    bass.notes.append(note)
for note in bass_notes_bar3:
    bass.notes.append(note)
for note in bass_notes_bar4:
    bass.notes.append(note)

for note in piano_notes:
    piano.notes.append(note)
for note in piano_notes_bar3:
    piano.notes.append(note)
for note in piano_notes_bar4:
    piano.notes.append(note)

for note in sax_notes:
    sax.notes.append(note)
for note in sax_notes_bar3:
    sax.notes.append(note)
for note in sax_notes_bar4:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
