
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in D minor, chromatic approaches
bass_notes = [
    (1.5, 62),  # D3
    (1.875, 60), # Bb3 (chromatic approach)
    (2.25, 62),  # D3
    (2.625, 64), # E3
    (2.875, 62), # D3
    (3.25, 60),  # Bb3
    (3.625, 62), # D3
    (4.0, 64),   # E3
    (4.25, 62),  # D3
    (4.625, 60), # Bb3
    (5.0, 62),   # D3
    (5.375, 64), # E3
    (5.625, 62), # D3
    (6.0, 60)    # Bb3
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25))

# Diane: 7th chords on 2 and 4, comping around the sax line
# Dm7 (D, F, A, C) on beat 2 of bar 2 and 4
piano_notes = [
    (2.0, 62), (2.0, 65), (2.0, 67), (2.0, 69),  # Dm7 (D, F, A, C)
    (3.0, 62), (3.0, 65), (3.0, 67), (3.0, 69),  # Dm7
    (4.0, 62), (4.0, 65), (4.0, 67), (4.0, 69),  # Dm7
    (5.0, 62), (5.0, 65), (5.0, 67), (5.0, 69)   # Dm7
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25))

# Dante: Sax motif - start it, leave it hanging, come back and finish it
# Motif: D (62) - F (65) - A (67) - D (62) -> leave it hanging on A at 2.25
# Then return with D (62) - F (65) - A (67) - D (62) at 5.0
sax_notes = [
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 62),  # Start of motif
    (2.25, 67), (2.25, 67), (2.25, 67), (2.25, 67),  # Hanging on A
    (5.0, 62), (5.0, 65), (5.0, 67), (5.0, 62)  # Return and finish
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Little Ray: Full kit in bars 2-4
# Kick on 1 and 3
for i in range(2, 6):
    kick_start = i * 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375))

# Snare on 2 and 4
for i in range(2, 6):
    snare_start = i * 0.375 + 0.75
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=snare_start, end=snare_start + 0.125))

# Hi-hat on every eighth
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.125
    sax.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
