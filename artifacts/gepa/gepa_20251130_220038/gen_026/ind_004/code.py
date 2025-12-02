
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.0625)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches, never the same note twice
# D Dorian: D, E, F#, G, A, B, C
bass_notes = [50, 52, 53, 55, 57, 59, 60]  # D, E, F#, G, A, B, C
bass_pattern = [50, 52, 53, 55, 57, 59, 60, 57, 55, 53, 52, 50, 52, 53, 55, 57]
for bar in range(2, 5):
    for i, note in enumerate(bass_pattern):
        time = bar * 1.5 + (i % 4) * 0.375
        note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
        bass.notes.append(note_obj)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# D7 = D, F#, A, C
# Dm7 = D, F, A, C
# G7 = G, B, D, F
# Bm7 = B, D, F#, A
piano_notes = [
    # Bar 2
    (50, 52, 57, 60),  # D7
    (50, 52, 57, 60),
    (50, 52, 57, 60),
    (50, 52, 57, 60),
    # Bar 3
    (50, 52, 57, 60),
    (50, 52, 57, 60),
    (50, 52, 57, 60),
    (50, 52, 57, 60),
    # Bar 4
    (50, 52, 57, 60),
    (50, 52, 57, 60),
    (50, 52, 57, 60),
    (50, 52, 57, 60),
]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            for pitch in piano_notes[(bar - 2) * 4 + beat]:
                note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
                piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D, F#, A, E
sax_notes = [50, 53, 57, 58]
sax_durations = [0.375, 0.375, 0.375, 0.375]
for i, note in enumerate(sax_notes):
    time = 1.5 + i * 0.375
    note_obj = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + sax_durations[i])
    sax.notes.append(note_obj)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
