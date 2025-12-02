
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Dm7: D F A C
# Walking bass line in Dm: D -> F -> Eb -> E -> F -> G -> A -> Bb -> B -> C -> Db -> D
bass_notes = [
    (1.5, 50),  # D
    (1.875, 53), # F
    (2.25, 51), # Eb
    (2.625, 52), # E
    (3.0, 53),  # F
    (3.375, 55), # G
    (3.75, 57),  # A
    (4.125, 58), # Bb
    (4.5, 59),  # B
    (4.875, 60), # C
    (5.25, 58),  # Db
    (5.625, 50)  # D
]
for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
# Dm7: D F A C
# Bars 2: comp on beat 2 and 4
# Bars 3: same
# Bars 4: same
diane_notes = [
    # Bar 2
    (1.875, 62), # F
    (1.875, 65), # A
    (1.875, 67), # C
    (1.875, 69), # D
    (2.25, 62), # F
    (2.25, 65), # A
    (2.25, 67), # C
    (2.25, 69), # D
    # Bar 3
    (3.375, 62), # F
    (3.375, 65), # A
    (3.375, 67), # C
    (3.375, 69), # D
    (3.75, 62), # F
    (3.75, 65), # A
    (3.75, 67), # C
    (3.75, 69), # D
    # Bar 4
    (4.875, 62), # F
    (4.875, 65), # A
    (4.875, 67), # C
    (4.875, 69), # D
    (5.25, 62), # F
    (5.25, 65), # A
    (5.25, 67), # C
    (5.25, 69), # D
]
for time, pitch in diane_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D -> Eb -> F -> D (Dm7 arpeggio with a twist)
# Bar 2: D (beat 1), Eb (beat 2), F (beat 3), rest (beat 4)
# Bar 3: D (beat 1), F (beat 2), G (beat 3), rest (beat 4)
# Bar 4: Eb (beat 1), D (beat 2), F (beat 3), D (beat 4)
sax_notes = [
    # Bar 2
    (1.5, 62), # D
    (1.875, 64), # Eb
    (2.25, 65), # F
    # Bar 3
    (3.0, 62), # D
    (3.375, 65), # F
    (3.75, 67), # G
    # Bar 4
    (4.5, 64), # Eb
    (4.875, 62), # D
    (5.25, 65), # F
    (5.625, 62)  # D
]
for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
