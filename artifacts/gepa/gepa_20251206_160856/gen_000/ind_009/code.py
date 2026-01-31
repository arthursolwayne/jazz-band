
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
bar_length = 1.5
kick_time = 0.0
snare_time = 0.75
hihat_time = 0.0
for i in range(4):
    drums.notes.append(pretty_midi.Note(100, 36, kick_time, kick_time + 0.1))
    drums.notes.append(pretty_midi.Note(100, 38, snare_time, snare_time + 0.1))
    for j in range(8):
        drums.notes.append(pretty_midi.Note(100, 42, hihat_time, hihat_time + 0.05))
        hihat_time += 0.125
    kick_time += 0.75
    snare_time += 0.75
    hihat_time = i * bar_length + 0.0

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
# F7 - Bb7 - E7 - A7
bass_notes = [
    (38, 1.5, 1.55),  # F
    (41, 1.75, 1.8),  # A
    (38, 2.0, 2.05),  # F
    (40, 2.25, 2.3),  # G
    (39, 2.5, 2.55),  # Ab
    (41, 2.75, 2.8),  # A
    (40, 3.0, 3.05),  # G
    (42, 3.25, 3.3),  # Bb
    (42, 3.5, 3.55),  # Bb
    (44, 3.75, 3.8),  # D
    (42, 4.0, 4.05),  # Bb
    (43, 4.25, 4.3),  # C
    (44, 4.5, 4.55),  # D
    (46, 4.75, 4.8),  # E
    (46, 5.0, 5.05),  # E
    (48, 5.25, 5.3),  # G
    (48, 5.5, 5.55),  # G
    (50, 5.75, 5.8),  # A
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note[0], note[1], note[2]))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (62, 1.5, 1.55),  # F
    (66, 1.5, 1.55),  # A
    (64, 1.5, 1.55),  # C
    (68, 1.5, 1.55),  # E
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    (60, 2.0, 2.05),  # Bb
    (64, 2.0, 2.05),  # D
    (62, 2.0, 2.05),  # F
    (65, 2.0, 2.05),  # Ab
]
# Bar 4: E7 (E, G#, B, D)
piano_notes += [
    (67, 2.5, 2.55),  # E
    (71, 2.5, 2.55),  # G#
    (69, 2.5, 2.55),  # B
    (72, 2.5, 2.55),  # D
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note[0], note[1], note[2]))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_time = 1.5
snare_time = 2.25
hihat_time = 1.5
for i in range(3):
    drums.notes.append(pretty_midi.Note(100, 36, kick_time, kick_time + 0.1))
    drums.notes.append(pretty_midi.Note(100, 38, snare_time, snare_time + 0.1))
    for j in range(8):
        drums.notes.append(pretty_midi.Note(100, 42, hihat_time, hihat_time + 0.05))
        hihat_time += 0.125
    kick_time += 0.75
    snare_time += 0.75
    hihat_time = 1.5 + i * bar_length + 0.0

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (62) - Ab (65) - C (64) - Eb (67) - F (62)
sax_notes = [
    (62, 1.5, 1.55),  # F
    (65, 1.625, 1.675),  # Ab
    (64, 1.75, 1.8),  # C
    (67, 1.875, 1.925),  # Eb
    (62, 2.0, 2.05),  # F
    (62, 3.0, 3.05),  # F (return)
    (65, 3.125, 3.175),  # Ab
    (64, 3.25, 3.3),  # C
    (67, 3.375, 3.425),  # Eb
    (62, 3.5, 3.55),  # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(100, note[0], note[1], note[2]))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
