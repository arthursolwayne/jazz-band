
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Sax enters with motif (1.5 - 3.0s)
# Motif: D4 (E4 grace), F4, G4, Bb4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.05),  # grace
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2 (approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=3.0),   # Ab2 (approach)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last bar
# Bar 2: D7 (G, B, D, F#) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.875),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C#5
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # D5
]

# Bar 3: G7 (B, D, F#, G) - open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # C#5
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.625),  # E5
])

# Bar 4: C7 (E, G, B, C) - open voicing
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # E5
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),  # G5
    pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=3.375),  # A5
])

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums continue (3.0 - 4.5s)
# Similar to bar 1, just shifted
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 1.5, note.end + 1.5)
    drums.notes.append(new_note)

# Bar 4: Drums continue (4.5 - 6.0s)
for note in drum_notes:
    new_note = pretty_midi.Note(note.velocity, note.pitch, note.start + 3.0, note.end + 3.0)
    drums.notes.append(new_note)

# Bar 3: Sax continues (3.0 - 4.5s)
# Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.0 + 0.05),  # grace
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Sax resolves (4.5 - 6.0s)
# End of motif, resolution to D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.05),  # grace
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=80, pitch=73, start=3.375, end=3.75),  # E5
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),  # G5
    pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.5),   # A5
    pretty_midi.Note(velocity=80, pitch=79, start=4.5, end=4.875),  # B5
    pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.25), # C#6
    pretty_midi.Note(velocity=80, pitch=81, start=5.25, end=5.625), # C#6
    pretty_midi.Note(velocity=80, pitch=79, start=5.625, end=6.0),  # B5
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Bar 4 resolution
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # E5
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # F#5
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=90, pitch=80, start=4.5, end=4.875),  # A5
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
