
import pretty_midi

# Create the MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42)
]
for start, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(note)

# Bass (Marcus): Walking line in F, roots and fifths with chromatic approaches
# F = 70, C = 67, B = 71, F = 70, E = 69, F = 70, D = 69, C = 67
bass_notes = [
    (1.5, 67), (1.875, 69), (2.25, 70), (2.625, 67),
    (3.0, 69), (3.375, 70), (3.75, 67), (4.125, 65)
]
for start, note in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# F7 (F A C E), Bm7b5 (B D F A), E7 (E G# B D), Fmaj7 (F A C E)
piano_notes = [
    # Bar 2: F7 (F A C E)
    (1.5, 70), (1.5, 69), (1.5, 67), (1.5, 72),
    # Bar 3: Bm7b5 (B D F A)
    (2.25, 71), (2.25, 67), (2.25, 69), (2.25, 69),
    # Bar 4: E7 (E G# B D)
    (3.0, 69), (3.0, 71), (3.0, 73), (3.0, 71),
    # Bar 4: Fmaj7 (F A C E)
    (3.75, 70), (3.75, 69), (3.75, 67), (3.75, 72)
]
for start, note in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (70) -> G (71) -> A (72) -> F (70) -> G (71) -> A (72) -> F (70)
sax_notes = [
    (1.5, 70), (1.875, 71), (2.25, 72), (2.625, 70),  # First phrase
    (3.0, 71), (3.375, 72), (3.75, 70)               # Second phrase
]
for start, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
