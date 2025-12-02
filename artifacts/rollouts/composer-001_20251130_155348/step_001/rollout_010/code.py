
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
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    (1.5, 62, 100), # D4
    (1.875, 63, 100), # Eb4
    (2.25, 64, 100), # E4
    (2.625, 65, 100), # F4
    (3.0, 67, 100), # G4
    (3.375, 65, 100), # F4
    (3.75, 64, 100), # E4
    (4.125, 62, 100), # D4
    (4.5, 60, 100), # C4
    (4.875, 62, 100), # D4
    (5.25, 64, 100), # E4
    (5.625, 65, 100), # F4
    (6.0, 67, 100), # G4
]
for start, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    (1.5, 62, 100), # D4
    (1.5, 67, 100), # F#4
    (1.5, 69, 100), # A4
    (1.5, 64, 100), # C4
    # Bar 3: G7 (G, B, D, F)
    (3.0, 67, 100), # G4
    (3.0, 71, 100), # B4
    (3.0, 62, 100), # D4
    (3.0, 69, 100), # F4
    # Bar 4: C7 (C, E, G, B)
    (4.5, 60, 100), # C4
    (4.5, 64, 100), # E4
    (4.5, 67, 100), # G4
    (4.5, 71, 100), # B4
]
for start, pitch, velocity in piano_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    piano.notes.append(note)

# Drums: Full pattern (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hi-hat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick3, snare2, snare4])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F# (67) - A (69) - D (62) - pause - D (62) - F# (67) - A (69) - C (64)
sax_notes = [
    (1.5, 62, 100), # D4
    (1.875, 67, 100), # F#4
    (2.25, 69, 100), # A4
    (2.625, 62, 100), # D4
    # Leave it hanging
    (3.0, 62, 100), # D4
    (3.375, 67, 100), # F#4
    (3.75, 69, 100), # A4
    (4.125, 64, 100), # C4
]
for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.375)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("waynes_shot.mid")
