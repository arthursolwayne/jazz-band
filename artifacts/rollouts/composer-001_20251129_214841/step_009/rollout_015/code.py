
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every 8th
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (1.5, 62, 0.375),  # C
    (1.875, 61, 0.375), # Bb
    (2.25, 64, 0.375),  # D
    (2.625, 66, 0.375), # E
    # Bar 3
    (2.875, 65, 0.375),  # Eb
    (3.25, 67, 0.375),   # F
    (3.625, 69, 0.375),  # G
    (4.0, 71, 0.375),    # A
    # Bar 4
    (4.375, 70, 0.375),  # Ab
    (4.75, 72, 0.375),   # Bb
    (5.125, 74, 0.375),  # C
    (5.5, 76, 0.375)     # D
]
for start, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 60, 0.375),  # C7 (C, E, B)
    (1.875, 64, 0.375),
    (1.875, 71, 0.375),
    # Bar 3
    (3.25, 60, 0.375),   # C7
    (3.25, 64, 0.375),
    (3.25, 71, 0.375),
    # Bar 4
    (4.75, 60, 0.375),   # C7
    (4.75, 64, 0.375),
    (4.75, 71, 0.375)
]
for start, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    piano.notes.append(note)

# Sax: Melody - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (1.5, 66, 0.375),  # E
    (1.875, 69, 0.375), # G
    (2.25, 67, 0.375),  # F
    (2.625, 66, 0.375), # E
    # Bar 3
    (3.0, 64, 0.375),   # D
    (3.375, 66, 0.375), # E
    (3.75, 69, 0.375),  # G
    # Bar 4
    (4.125, 67, 0.375), # F
    (4.5, 66, 0.375),   # E
    (4.875, 64, 0.375), # D
    (5.25, 62, 0.375)   # C
]
for start, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration)
    sax.notes.append(note)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every 8th
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write('dante_intro.mid')
