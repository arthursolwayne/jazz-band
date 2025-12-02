
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
    (0.0, 36, 100),  # Kick on beat 1
    (0.75, 42, 100), # Hihat on & of 1
    (1.0, 38, 100),  # Snare on beat 2
    (1.75, 42, 100), # Hihat on & of 2
    (2.0, 36, 100),  # Kick on beat 3
    (2.75, 42, 100), # Hihat on & of 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.75, 42, 100)  # Hihat on & of 4
]

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (1.5, 62, 100),  # D (root)
    (1.75, 61, 100), # C# (chromatic approach)
    (2.0, 64, 100),  # F (3rd)
    (2.25, 63, 100), # E (chromatic approach)
    (2.5, 67, 100),  # A (5th)
    (2.75, 66, 100), # G (chromatic approach)
    (3.0, 62, 100),  # D (root)
    (3.25, 61, 100), # C# (chromatic approach)
    (3.5, 64, 100),  # F (3rd)
    (3.75, 63, 100), # E (chromatic approach)
    (4.0, 67, 100),  # A (5th)
    (4.25, 66, 100), # G (chromatic approach)
    (4.5, 62, 100),  # D (root)
    (4.75, 61, 100), # C# (chromatic approach)
    (5.0, 64, 100),  # F (3rd)
    (5.25, 63, 100), # E (chromatic approach)
]

for start, note, velocity in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 62, 100),  # D
    (2.0, 67, 100),  # A
    (2.0, 69, 100),  # C
    (2.0, 71, 100),  # F
    # Bar 3
    (3.5, 62, 100),  # D
    (3.5, 67, 100),  # A
    (3.5, 69, 100),  # C
    (3.5, 71, 100),  # F
    # Bar 4
    (5.0, 62, 100),  # D
    (5.0, 67, 100),  # A
    (5.0, 69, 100),  # C
    (5.0, 71, 100),  # F
]

for start, note, velocity in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Drums: Bar 2-4
drum_notes = [
    (1.5, 36, 100),  # Kick on beat 1
    (2.0, 38, 100),  # Snare on beat 2
    (2.5, 36, 100),  # Kick on beat 3
    (3.0, 38, 100),  # Snare on beat 4
    (3.5, 36, 100),  # Kick on beat 1
    (4.0, 38, 100),  # Snare on beat 2
    (4.5, 36, 100),  # Kick on beat 3
    (5.0, 38, 100),  # Snare on beat 4
]

# Add hihat on every eighth
for i in range(2, 6):
    for j in range(1, 9):
        start = 1.5 + i * 0.5 + (j - 1) * 0.25
        if start < 6.0:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.25))

for start, note, velocity in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

# Sax: Motif in Dm, short and singable
sax_notes = [
    (1.5, 62, 100),  # D
    (1.75, 64, 100), # F
    (2.0, 65, 100),  # G
    (2.25, 62, 100), # D
    (2.5, 64, 100),  # F
    (2.75, 65, 100), # G
    (3.0, 62, 100),  # D
    (3.25, 64, 100), # F
    (3.5, 65, 100),  # G
    (3.75, 62, 100), # D
    (4.0, 64, 100),  # F
    (4.25, 65, 100), # G
    (4.5, 62, 100),  # D
    (4.75, 64, 100), # F
    (5.0, 65, 100),  # G
    (5.25, 67, 100), # A
]

for start, note, velocity in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=velocity, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
