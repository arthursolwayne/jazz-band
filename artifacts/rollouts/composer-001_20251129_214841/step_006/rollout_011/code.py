
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
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62),  # C4
    (1.875, 63), # C#4
    (2.25, 64),  # D4
    (2.625, 65), # D#4
    (3.0, 67),   # E4
    (3.375, 69), # F#4
    (3.75, 71),  # G#4
    (4.125, 72), # A4
    (4.5, 74),   # Bb4
    (4.875, 76), # B4
    (5.25, 77),  # B#4 (C5)
    (5.625, 79), # C#5
    (6.0, 81)    # D5
]
for note in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note[1], start=note[0], end=note[0] + 0.375)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
# C7 on beat 2 and 4 of bar 2
piano_notes = [
    (2.25, 60, 100),   # C4
    (2.25, 64, 100),   # E4
    (2.25, 67, 100),   # G4
    (2.25, 71, 100),   # B4
    # C7 on beat 4 of bar 2
    (3.0, 60, 100),
    (3.0, 64, 100),
    (3.0, 67, 100),
    (3.0, 71, 100),
    # C7 on beat 2 of bar 3
    (3.75, 60, 100),
    (3.75, 64, 100),
    (3.75, 67, 100),
    (3.75, 71, 100),
    # C7 on beat 4 of bar 3
    (4.5, 60, 100),
    (4.5, 64, 100),
    (4.5, 67, 100),
    (4.5, 71, 100),
    # C7 on beat 2 of bar 4
    (5.25, 60, 100),
    (5.25, 64, 100),
    (5.25, 67, 100),
    (5.25, 71, 100),
    # C7 on beat 4 of bar 4
    (6.0, 60, 100),
    (6.0, 64, 100),
    (6.0, 67, 100),
    (6.0, 71, 100)
]
for note in piano_notes:
    piano_note = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    piano.notes.append(piano_note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(0, 8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C (60) - E (64) - G (67) - B (71)
# Start at bar 2 (1.5s)
sax_notes = [
    (1.5, 60, 100),   # C4
    (1.875, 64, 100), # E4
    (2.25, 67, 100),  # G4
    (2.625, 71, 100), # B4
    (3.0, 67, 100),   # G4 (hold)
    (3.375, 67, 100), # G4
    (3.75, 67, 100),  # G4
    (4.125, 67, 100), # G4
    (4.5, 60, 100),   # C4
    (4.875, 64, 100), # E4
    (5.25, 67, 100),  # G4
    (5.625, 71, 100), # B4
    (6.0, 71, 100)    # B4 (hold)
]
for note in sax_notes:
    sax_note = pretty_midi.Note(velocity=note[2], pitch=note[1], start=note[0], end=note[0] + 0.375)
    sax.notes.append(sax_note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
