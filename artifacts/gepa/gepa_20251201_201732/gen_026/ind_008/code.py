
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
kick_time = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
snare_time = [0.375, 1.125, 1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
hihat_time = [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125,
              1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125,
              3.0, 3.1875, 3.375, 3.5625, 3.75, 3.9375, 4.125, 4.3125,
              4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]

# Add drum notes
for t in kick_time:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.125))
for t in snare_time:
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.125))
for t in hihat_time:
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    (1.5, 43),  # G2
    (1.75, 41),  # E2
    (2.0, 42),   # F2
    (2.25, 43),  # G2
    (2.5, 45),   # A2
    (2.75, 43),  # G2
    (3.0, 42),   # F2
]
for t, p in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=p, start=t, end=t + 0.25))

# Piano: Open voicings, one chord per bar, resolve on last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (1.5, 71),  # F4
    (1.5, 76),  # A4
    (1.5, 72),  # C4
    (1.5, 74),  # E4
    (1.75, 71), # F4
    (1.75, 76), # A4
    (1.75, 72), # C4
    (1.75, 74), # E4
    (2.0, 71),  # F4
    (2.0, 76),  # A4
    (2.0, 72),  # C4
    (2.0, 74),  # E4
    (2.25, 71), # F4
    (2.25, 78), # C#5
    (2.25, 74), # E4
    (2.25, 76), # A4
]
for t, p in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: F4 - Ab4 - Bb4 - F4 (in bar 2), then finish in bar 4
sax_notes = [
    (1.5, 71),  # F4
    (1.625, 70), # Eb4 (chromatic)
    (1.75, 72),  # G4 (but we play Bb4 = 71-1 = 70?)
    (1.875, 71), # F4 again
    (2.5, 71),  # F4
    (2.625, 70), # Eb4
    (2.75, 72),  # G4
    (2.875, 71), # F4
    (3.5, 71),  # F4 (end)
]
for t, p in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=p, start=t, end=t + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    (3.0, 42),   # F2
    (3.25, 40),  # D2
    (3.5, 41),   # E2
    (3.75, 42),  # F2
    (4.0, 44),   # G2
    (4.25, 42),  # F2
    (4.5, 41),   # E2
]
for t, p in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=p, start=t, end=t + 0.25))

# Piano: Open voicings, one chord per bar, resolve on last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    (3.0, 67),  # Bb4
    (3.0, 72),  # D5
    (3.0, 71),  # C4 (F4)
    (3.0, 70),  # Eb4
    (3.25, 67), # Bb4
    (3.25, 72), # D5
    (3.25, 71), # C4
    (3.25, 70), # Eb4
    (3.5, 67),  # Bb4
    (3.5, 72),  # D5
    (3.5, 71),  # C4
    (3.5, 70),  # Eb4
    (3.75, 67), # Bb4
    (3.75, 74), # E5
    (3.75, 70), # Eb4
    (3.75, 72), # D5
]
for t, p in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25))

# Sax: Motif continuation
sax_notes = [
    (3.0, 70),  # Eb4
    (3.125, 71), # F4
    (3.25, 72),  # G4
    (3.375, 71), # F4 again
    (3.5, 71),   # F4
    (3.625, 70), # Eb4
    (3.75, 72),  # G4
    (3.875, 71), # F4
    (4.0, 71),   # F4
]
for t, p in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=p, start=t, end=t + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    (4.5, 41),   # E2
    (4.75, 43),  # G2
    (5.0, 42),   # F2
    (5.25, 41),  # E2
    (5.5, 40),   # D2
    (5.75, 41),  # E2
    (6.0, 42),   # F2
]
for t, p in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=p, start=t, end=t + 0.25))

# Piano: Open voicings, one chord per bar, resolve on last
# Bar 4: C7 (C, E, G, B)
piano_notes = [
    (4.5, 72),  # C5
    (4.5, 74),  # E5
    (4.5, 76),  # G5
    (4.5, 79),  # B5
    (4.75, 72), # C5
    (4.75, 74), # E5
    (4.75, 76), # G5
    (4.75, 79), # B5
    (5.0, 72),  # C5
    (5.0, 74),  # E5
    (5.0, 76),  # G5
    (5.0, 79),  # B5
    (5.25, 72), # C5
    (5.25, 77), # A5
    (5.25, 79), # B5
    (5.25, 76), # G5
]
for t, p in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=p, start=t, end=t + 0.25))

# Sax: Finish the motif
sax_notes = [
    (4.5, 70),  # Eb4
    (4.625, 71), # F4
    (4.75, 72),  # G4
    (4.875, 71), # F4
    (5.0, 71),   # F4
    (5.125, 70), # Eb4
    (5.25, 72),  # G4
    (5.375, 71), # F4
    (5.5, 71),   # F4 (end)
]
for t, p in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=p, start=t, end=t + 0.125))

# Add the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
