
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
drum_notes = [
    (36, 0.0),    # Kick on 1
    (38, 0.5),    # Snare on 2
    (36, 1.0),    # Kick on 3
    (38, 1.5),    # Snare on 4
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Hihat on every eighth note
for i in range(8):
    time = i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line: D2, G2, A2, C3, B2, G2, F2, D2
bass_notes = [
    (38, 1.5),  # D2
    (43, 1.75), # G2
    (45, 2.0),  # A2
    (48, 2.25), # C3
    (47, 2.5),  # B2
    (43, 2.75), # G2
    (42, 3.0),  # F2
    (38, 3.25)  # D2
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Diane - Open voicings, resolving on the last bar
# Bar 2: Dm7 (F, A, D, G)
# Bar 3: G7 (B, D, G, F)
# Bar 4: Cm7 (E, G, C, B)
piano_notes = [
    # Bar 2
    (57, 1.5),  # G
    (62, 1.5),  # D
    (65, 1.5),  # A
    (67, 1.5),  # F
    # Bar 3
    (67, 2.0),  # G
    (69, 2.0),  # B
    (71, 2.0),  # D
    (65, 2.0),  # F
    # Bar 4
    (60, 2.5),  # C
    (64, 2.5),  # E
    (67, 2.5),  # G
    (71, 2.5),  # B
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Dante - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 - D, F, A, Bb
# Play D on 1, F on 2, A on 3, and leave Bb (Bb is Bb on the 4th beat)
# Then repeat the motif on the next bar but end it with Bb
sax_notes = [
    # Bar 2
    (62, 1.5),  # D
    (65, 1.75), # F
    (67, 2.0),  # A
    (62, 2.5),  # D
    (65, 2.75), # F
    (67, 3.0),  # A
    (60, 3.25)  # Bb (Dm7 altered)
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Walking bass line: G2, C3, D3, F3, E3, C3, B2, G2
bass_notes = [
    (43, 3.0),  # G2
    (48, 3.25), # C3
    (50, 3.5),  # D3
    (53, 3.75), # F3
    (51, 4.0),  # E3
    (48, 4.25), # C3
    (47, 4.5),  # B2
    (43, 4.75)  # G2
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Diane - Open voicings, resolving on the last bar
# Bar 3: G7 (B, D, G, F)
# Bar 4: Cm7 (E, G, C, B)
piano_notes = [
    # Bar 3
    (69, 3.0),  # B
    (71, 3.0),  # D
    (76, 3.0),  # G
    (65, 3.0),  # F
    # Bar 4
    (60, 3.5),  # C
    (64, 3.5),  # E
    (67, 3.5),  # G
    (71, 3.5),  # B
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Dante - Motif continuation and resolution
# Repeat and resolve with Bb on the last beat
sax_notes = [
    # Bar 3
    (62, 3.0),  # D
    (65, 3.25), # F
    (67, 3.5),  # A
    (60, 4.0),  # Bb
]
for note, time in sax_notes:
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1)
    sax.notes.append(note_obj)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Walking bass line: C3, E3, F3, A3, G3, E3, D3, C3
bass_notes = [
    (48, 4.5),  # C3
    (51, 4.75), # E3
    (52, 5.0),  # F3
    (57, 5.25), # A3
    (55, 5.5),  # G3
    (51, 5.75), # E3
    (50, 6.0),  # D3
    (48, 6.15)  # C3
]
for note, time in bass_notes:
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

# Diane - Open voicings, resolving on the last bar
# Bar 4: Cm7 (E, G, C, B)
piano_notes = [
    (64, 4.5),  # E
    (67, 4.5),  # G
    (60, 4.5),  # C
    (71, 4.5),  # B
]
for note, time in piano_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    piano.notes.append(note_obj)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5),    # Kick on 1
    (38, 5.0),    # Snare on 2
    (36, 5.5),    # Kick on 3
    (38, 6.0),    # Snare on 4
]
for note, time in drum_notes:
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

# Hihat on every eighth note
for i in range(8):
    time = 4.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
