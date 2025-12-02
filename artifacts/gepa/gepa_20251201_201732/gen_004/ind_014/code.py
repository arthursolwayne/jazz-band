
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
for i in range(4):
    time = i * bar_length / 4
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.1)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, roots and fifths with chromatic approaches
# D2 (D), F2 (F), A2 (A), C2 (C), chromatic approaches
bass_notes = [
    (1.5, 38, 0.25),  # D2
    (2.0, 40, 0.25),  # Eb2 (chromatic approach to F2)
    (2.5, 43, 0.25),  # F2
    (3.0, 45, 0.25),  # G2 (chromatic approach to A2)
    (3.5, 47, 0.25),  # A2
    (4.0, 49, 0.25),  # Bb2 (chromatic approach to B2)
    (4.5, 50, 0.25),  # B2
    (5.0, 52, 0.25)   # C2
]
for time, pitch, duration in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar
# Bar 2: Dm7 (F, A, D, G)
# Bar 3: G7 (B, D, F#, G)
# Bar 4: Cm7 (Eb, G, C, E)
# Comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5-3.0s)
    (1.5, 62, 0.25),  # G4
    (1.5, 65, 0.25),  # B4
    (1.5, 69, 0.25),  # D5
    (1.5, 71, 0.25),  # F#5
    # Bar 3 (3.0-4.5s)
    (3.0, 64, 0.25),  # Eb4
    (3.0, 67, 0.25),  # G4
    (3.0, 72, 0.25),  # C5
    (3.0, 76, 0.25),  # E5
    # Bar 4 (4.5-6.0s)
    (4.5, 62, 0.25),  # G4
    (4.5, 65, 0.25),  # B4
    (4.5, 69, 0.25),  # D5
    (4.5, 71, 0.25)   # F#5
]
for time, pitch, duration in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, B, C
# Motif: D (62), F (64), A (67), D (62) -> then G (67), Bb (69), D (62)
sax_notes = [
    (1.5, 62, 0.5),  # D4
    (2.0, 64, 0.5),  # F4
    (2.5, 67, 0.5),  # A4
    (3.0, 62, 0.5),  # D4 (end of first phrase)
    (3.5, 67, 0.5),  # G4
    (4.0, 69, 0.5),  # Bb4
    (4.5, 62, 1.0)   # D4 (resolve)
]
for time, pitch, duration in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Drums continue with same pattern for bars 2-4
for i in range(4):
    time = 1.5 + (i * bar_length / 4)
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.1)
    drums.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
