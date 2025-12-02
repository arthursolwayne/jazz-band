
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick3, snare2, snare4, hihat1, hihat2, hihat3, hihat4])

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 59),  # D
    (1.875, 60), # Eb
    (2.25, 62),  # F
    (2.625, 61), # E
    (3.0, 60),   # Eb
    (3.375, 58), # D
    (3.75, 59),  # D
    (4.125, 60), # Eb
    (4.5, 62),   # F
    (4.875, 61), # E
    (5.25, 60),  # Eb
    (5.625, 59), # D
]
for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 62),  # F
    (1.875, 67),  # Bb
    (1.875, 64),  # D
    (1.875, 69),  # G
    (3.375, 62),  # F
    (3.375, 67),  # Bb
    (3.375, 64),  # D
    (3.375, 69),  # G
    (4.875, 62),  # F
    (4.875, 67),  # Bb
    (4.875, 64),  # D
    (4.875, 69),  # G
]
for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 (D, F, A, C) with some chromaticism
sax_notes = [
    (1.5, 62),    # D
    (1.625, 61),  # C
    (1.75, 62),   # D
    (1.875, 64),  # F
    (2.25, 62),   # D
    (2.625, 64),  # F
    (3.0, 66),    # G
    (3.375, 64),  # F
    (3.75, 62),   # D
    (4.125, 61),  # C
    (4.5, 62),    # D
    (4.875, 64),  # F
    (5.25, 66),   # G
    (5.625, 64),  # F
]
for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("dm_intro.mid")
