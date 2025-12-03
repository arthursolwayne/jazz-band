
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
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.75),  # D2
    pretty_midi.Note(velocity=100, pitch=40, start=1.75, end=2.0),  # F2
    pretty_midi.Note(velocity=100, pitch=41, start=2.0, end=2.25),  # F#2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.5),  # G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.75),  # F#2
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0),  # D2
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0),  # C#5
]

# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C#5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # E5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # F5
])

# Bar 4: C7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
])

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 3 (3.0 - 4.5)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4 (4.5 - 6.0)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: D4, F#4, G4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # G4
]

# Bar 3: D4, F#4, G4, D5
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.0),  # D5
])

# Bar 4: F#4, G4, A4, D5
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # D5
])

for note in sax_notes:
    sax.notes.append(note)

# Add hihat on every eighth note
for bar in range(4):
    for eighth in range(8):
        start = bar * 1.5 + (eighth * 0.375)
        end = start + 0.375
        if bar == 0:
            continue  # No hihat in bar 1
        else:
            hihat_note = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
            drums.notes.append(hihat_note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
