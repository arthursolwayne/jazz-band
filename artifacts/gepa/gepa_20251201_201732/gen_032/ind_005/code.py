
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # F#2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C#5
]
# Bar 3: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # F#5
])
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),   # C4
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # E4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # B4
])
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, E4, F#4, D4 (on 1, 2, 3, 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line again, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D2 (start of bar 3)
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),  # Eb2
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=80, pitch=66, start=4.125, end=4.5),   # F#2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # F#5
]
# Bar 4: C7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),   # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),   # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),   # B4
])
# End on C7 (resolve)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.5),   # C4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.5),   # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.5),   # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.5),   # B4
])
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line again, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=80, pitch=66, start=5.625, end=6.0),   # F#2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 4: D7 (resolve to D7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C#5
]
for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
