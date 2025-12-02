
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 100), # Hihat on 2
    (1.5, 38, 100),  # Snare on 3
    (2.25, 42, 100), # Hihat on 4
    (3.0, 36, 100),  # Kick on 1 (bar 2)
    (3.75, 42, 100), # Hihat on 2
    (4.5, 38, 100),  # Snare on 3
    (5.25, 42, 100), # Hihat on 4
    (6.0, 36, 100),  # Kick on 1 (bar 3)
    (6.75, 42, 100), # Hihat on 2
    (7.5, 38, 100),  # Snare on 3
    (8.25, 42, 100), # Hihat on 4
    (9.0, 36, 100),  # Kick on 1 (bar 4)
    (9.75, 42, 100), # Hihat on 2
    (10.5, 38, 100), # Snare on 3
    (11.25, 42, 100) # Hihat on 4
]
for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    (1.5, 60, 100), (1.75, 61, 100), (2.0, 62, 100), (2.25, 63, 100),
    (2.5, 64, 100), (2.75, 63, 100), (3.0, 62, 100), (3.25, 61, 100),
    (3.5, 60, 100), (3.75, 61, 100), (4.0, 62, 100), (4.25, 63, 100),
    (4.5, 64, 100), (4.75, 65, 100), (5.0, 66, 100), (5.25, 65, 100),
    (5.5, 64, 100), (5.75, 63, 100), (6.0, 62, 100)
]
for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    (2.0, 60, 100), (2.0, 64, 100), (2.0, 67, 100),
    # Bar 2: F7 on beat 4
    (3.0, 65, 100), (3.0, 69, 100), (3.0, 71, 100),
    # Bar 3: G7 on beat 2
    (3.5, 67, 100), (3.5, 71, 100), (3.5, 74, 100),
    # Bar 3: C7 on beat 4
    (4.5, 60, 100), (4.5, 64, 100), (4.5, 67, 100),
    # Bar 4: E7 on beat 2
    (5.0, 64, 100), (5.0, 68, 100), (5.0, 71, 100),
    # Bar 4: A7 on beat 4
    (6.0, 69, 100), (6.0, 73, 100), (6.0, 76, 100)
]
for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Sax (Dante) - short motif, start on bar 2
sax_notes = [
    (2.0, 62, 100), (2.25, 64, 100), (2.5, 62, 100),
    (3.5, 62, 100), (3.75, 64, 100), (4.0, 62, 100),
    (5.0, 62, 100), (5.25, 64, 100), (5.5, 62, 100)
]
for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
