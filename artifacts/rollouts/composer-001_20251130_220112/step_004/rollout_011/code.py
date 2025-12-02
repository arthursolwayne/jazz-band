
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),  # Dm7 root
    (1.875, 63), # chromatic up
    (2.25, 60), # Dm7 5th
    (2.625, 59), # chromatic down
    (3.0, 62),  # Dm7 root
    (3.375, 63), # chromatic up
    (3.75, 60), # Dm7 5th
    (4.125, 59), # chromatic down
    (4.5, 62),  # Dm7 root
    (4.875, 63), # chromatic up
    (5.25, 60), # Dm7 5th
    (5.625, 59) # chromatic down
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 62), # Dm7 root
    (1.875, 67), # Bb
    (1.875, 69), # F
    (1.875, 71), # A
    (3.375, 62), # Dm7 root
    (3.375, 67), # Bb
    (3.375, 69), # F
    (3.375, 71), # A
    (4.875, 62), # Dm7 root
    (4.875, 67), # Bb
    (4.875, 69), # F
    (4.875, 71)  # A
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Start with a Dm7 phrase: D (62), F (65), Bb (67), D (62), leave it hanging on the Bb (67)
sax_notes = [
    (1.5, 62), # D
    (1.625, 65), # F
    (1.75, 67), # Bb
    (1.875, 62), # D
    (2.25, 67) # Bb (hang)
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125)
    sax.notes.append(note)

# End of the motif
sax_notes = [
    (3.0, 62), # D
    (3.125, 65), # F
    (3.25, 67), # Bb
    (3.5, 62) # D
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.125)
    sax.notes.append(note)

# Drums in bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.0, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
