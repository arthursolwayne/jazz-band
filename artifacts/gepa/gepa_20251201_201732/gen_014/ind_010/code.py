
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

# Bar 2
# Marcus: Walking bass line in F (F2, C3, G2, D3, Eb3, Bb2, Ab2, F2)
for i, pitch in enumerate([77, 84, 78, 81, 80, 75, 73, 77]):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
notes = [77, 82, 84, 87]
for i, pitch in enumerate(notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=1.5 + 1.5)
    piano.notes.append(note)

# Bar 3: Bb7 (Bb, D, F, Ab)
notes = [74, 79, 82, 73]
for i, pitch in enumerate(notes):
    time = 1.5 + 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=1.5 + 3.0)
    piano.notes.append(note)

# Bar 4: Eb7 (Eb, G, Bb, D)
notes = [73, 78, 80, 79]
for i, pitch in enumerate(notes):
    time = 1.5 + 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=1.5 + 4.5)
    piano.notes.append(note)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G, Eb, F (bar 2), then repeat in bar 4
# Bar 2: F (77), G (79), Eb (73), F (77)
for i, pitch in enumerate([77, 79, 73, 77]):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Bar 4: repeat the motif
for i, pitch in enumerate([77, 79, 73, 77]):
    time = 1.5 + 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

# Drums: continue the pattern
for bar in range(2, 4):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
